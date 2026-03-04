/* Multilingual Docs - Main JS */
(function () {
  'use strict';

  /* ================================================================
     WASM MODULE LOADER
     Lazily instantiates assets/wasm/multilingual.wasm — the demo.ml
     program compiled to WASM by `multilingual build-wasm-bundle` via
     WATCodeGenerator (multilingualprogramming[wasm]).

     The WAT backend uses host-import callbacks for all output rather
     than returning values.  The browser must supply these imports:

       env.print_str(ptr: i32, len: i32)  — print a UTF-8 string slice
       env.print_f64(val: f64)            — print a number
       env.print_bool(val: i32)           — print True (1) or False (0)
       env.print_sep()                    — print an argument separator (space)
       env.print_newline()                — print a newline

     Output is captured into a string buffer that is reset before each
     call to __main().

     The Run buttons on individual code examples call __main() and show
     the captured output.  For a fully interactive experience with
     arbitrary code, visit the live playground linked on the WASM page.

     The loader resolves the base URL from the <meta name="base-url"> tag
     so paths work identically on local dev and under /docs on GitHub Pages.
     ================================================================ */

  const baseUrl = (document.querySelector('meta[name="base-url"]') || {}).content || '';

  const MLWasm = (() => {
    let _memory        = null;
    let _outputBuf     = '';
    let _modulePromise = null;

    const dec = new TextDecoder();

    /* Build a host import object whose callbacks write into `bufRef`.
     * Using an object reference lets us set `bufRef.mem` after instantiation
     * while keeping the closure intact. */
    function makeImports(bufRef) {
      return {
        env: {
          print_str(ptr, len) {
            bufRef.v += dec.decode(new Uint8Array(bufRef.mem.buffer, ptr, len));
          },
          print_f64(val)  { bufRef.v += String(val); },
          print_bool(val) { bufRef.v += val ? 'True' : 'False'; },
          print_sep()     { bufRef.v += ' '; },
          print_newline() { bufRef.v += '\n'; },
        },
      };
    }

    /* Host imports for the shared demo module (uses module-level state). */
    const importObject = {
      env: {
        print_str(ptr, len) {
          _outputBuf += dec.decode(new Uint8Array(_memory.buffer, ptr, len));
        },
        print_f64(val)  { _outputBuf += String(val); },
        print_bool(val) { _outputBuf += val ? 'True' : 'False'; },
        print_sep()     { _outputBuf += ' '; },
        print_newline() { _outputBuf += '\n'; },
      },
    };

    function load() {
      if (_modulePromise) return _modulePromise;

      const wasmUrl = baseUrl + '/assets/wasm/multilingual.wasm';

      _modulePromise = WebAssembly.instantiateStreaming(fetch(wasmUrl), importObject)
        .then(({ instance }) => {
          _memory = instance.exports.memory;
          return true;
        });

      return _modulePromise;
    }

    /* ---- WAT text loader ------------------------------------------------- */
    let _watPromise = null;

    function loadWat() {
      if (_watPromise) return _watPromise;
      const watUrl = baseUrl + '/assets/wasm/multilingual.wat';
      _watPromise = fetch(watUrl).then(r => {
        if (!r.ok) throw new Error(`WAT fetch failed: ${r.status}`);
        return r.text();
      });
      return _watPromise;
    }

    /* ---- Per-block WASM loader ------------------------------------------ */
    /* Each code block is compiled to its own binary during the CI build by
     * _scripts/compile_blocks.py.  The binary is identified by the first 16
     * hex characters of SHA-256(code), matching the hash computed here. */
    const _blockModules = new Map();  // hash16 → WebAssembly.Module | null

    async function blockHash(src) {
      const buf = await crypto.subtle.digest(
        'SHA-256', new TextEncoder().encode(src)
      );
      return Array.from(new Uint8Array(buf))
        .map(b => b.toString(16).padStart(2, '0'))
        .join('')
        .slice(0, 16);
    }

    async function loadBlockModule(hash16) {
      if (_blockModules.has(hash16)) return _blockModules.get(hash16);
      const url = baseUrl + '/assets/wasm/blocks/' + hash16 + '.wasm';
      try {
        const mod = await WebAssembly.compileStreaming(fetch(url));
        _blockModules.set(hash16, mod);
        return mod;
      } catch (_) {
        /* Binary not available for this block — will fall back to demo. */
        _blockModules.set(hash16, null);
        return null;
      }
    }

    /* Public API */
    return {
      /* Execute a specific code block: loads its per-block WASM binary.
       * hash16 is the pre-computed data-block-hash attribute injected at
       * build time by _scripts/inject_hashes.py — no browser-side hashing. */
      async execute(src, hash16) {
        if (!hash16) {
          return {
            stdout: '',
            stderr: 'This block could not be executed: no WASM binary was\n'
                  + 'compiled for it during the CI build (the compiler may not\n'
                  + 'yet support all constructs used here).\n'
                  + 'Try the REPL panel to run the full demo program.',
          };
        }
        const mod = await loadBlockModule(hash16);

        if (!mod) {
          /* No per-block binary available for this code.  Rather than
           * running the unrelated demo program, tell the user clearly. */
          return {
            stdout: '',
            stderr: 'This block could not be executed: no WASM binary was\n'
                  + 'compiled for it during the CI build (the compiler may not\n'
                  + 'yet support all constructs used here).\n'
                  + 'Try the REPL panel to run the full demo program.',
          };
        }

        /* Instantiate the per-block module with fresh state for each run. */
        const bufRef   = { v: '', mem: null };
        const instance = await WebAssembly.instantiate(mod, makeImports(bufRef));
        bufRef.mem = instance.exports.memory;
        bufRef.v   = '';
        try { instance.exports.__main(); }
        catch (e) { return { stdout: bufRef.v, stderr: String(e) }; }
        return { stdout: bufRef.v, stderr: '' };
      },
      /* Expose the load promise so the toggle button can show readiness. */
      get ready() { return load(); },
      /* Returns a Promise<string> with the WAT text format. */
      get wat()   { return loadWat(); },
    };
  })();


  /* ================================================================
     PYODIDE REPL
     Lazily loads Pyodide the first time the user opens the REPL panel,
     then uses ProgramExecutor(language=lang) to compile and execute
     arbitrary multilingual source code client-side.
     ================================================================ */

  let _pyodide      = null;
  let _pyodideReady = false;
  let _pyodideInit  = null;   // singleton Promise

  function _loadPyodideScript() {
    return new Promise((resolve, reject) => {
      if (typeof loadPyodide === 'function') { resolve(); return; }
      const s = document.createElement('script');
      s.src = 'https://cdn.jsdelivr.net/pyodide/v0.26.0/full/pyodide.js';
      s.onload  = resolve;
      s.onerror = () => reject(new Error('Failed to load Pyodide script'));
      document.head.appendChild(s);
    });
  }

  async function _initReplPyodide() {
    if (_pyodideReady) return;
    setReplStatus('loading', 'loading…');
    await _loadPyodideScript();

    _pyodide = await loadPyodide({    // eslint-disable-line no-undef
      indexURL: 'https://cdn.jsdelivr.net/pyodide/v0.26.0/full/',
    });
    setReplStatus('loading', 'installing…');
    await _pyodide.loadPackage('micropip');
    const micropip = _pyodide.pyimport('micropip');
    await micropip.install('roman');
    await micropip.install('python-dateutil');

    // Try a locally-built wheel first, fall back to PyPI
    let installed = false;
    try {
      const resp = await fetch(baseUrl + '/assets/wheel_info.json');
      if (resp.ok) {
        const info = await resp.json();
        const url  = new URL(baseUrl + '/assets/' + info.wheel, window.location.href).href;
        await micropip.install(url);
        installed = true;
      }
    } catch (_) { /* wheel_info.json absent — fall back to PyPI */ }

    if (!installed) {
      await micropip.install('multilingualprogramming');
    }

    // Warm-up import so the first Run is fast
    await _pyodide.runPythonAsync(
      'from multilingualprogramming.codegen.executor import ProgramExecutor'
    );

    _pyodideReady = true;
    setReplStatus('ready', 'ready');
  }

  function ensureReplPyodide() {
    if (!_pyodideInit) _pyodideInit = _initReplPyodide().catch(err => {
      setReplStatus('error', 'error');
      console.error('Pyodide init failed:', err);
      _pyodideInit = null;   // allow retry
    });
    return _pyodideInit;
  }

  /* ================================================================
     REPL PANEL
     ================================================================ */

  /* Language classes that identify shell/config blocks — not executable
     multilingual source.  All other fenced blocks get a Run button. */
  const NON_EXECUTABLE = new Set([
    'language-bash', 'language-sh', 'language-shell',
    'language-powershell', 'language-cmd',
    'language-js', 'language-javascript', 'language-markdown', 'language-dockerfile',
    'language-output', 'language-wat', 'language-rust',
    'language-yaml', 'language-toml', 'language-json',
    'language-plaintext', 'language-text',
  ]);

  function isExecutable(codeEl) {
    return [...codeEl.classList].every(c => !NON_EXECUTABLE.has(c));
  }

  function looksLikeHostPython(src) {
    return /^\s*(import\s+\w+|from\s+\w+\s+import\s+|#!\/usr\/bin\/env\s+python\d*(?:\.\d+)*)/m.test(src);
  }

  /* Render output (stdout + optional stderr) into a .code-output element. */
  function renderOutput(container, { stdout, stderr }) {
    container.innerHTML = '';
    if (stdout) {
      const pre = document.createElement('pre');
      pre.className = 'output-stdout';
      pre.textContent = stdout;
      container.appendChild(pre);
    }
    if (stderr) {
      const pre = document.createElement('pre');
      pre.className = 'output-stderr';
      pre.textContent = stderr;
      container.appendChild(pre);
    }
    if (!stdout && !stderr) {
      const span = document.createElement('span');
      span.className = 'output-empty';
      span.textContent = '(no output)';
      container.appendChild(span);
    }
  }

  /* Set the REPL status dot + badge text. */
  function setReplStatus(state, label) {
    const dot   = document.getElementById('repl-status-dot');
    const badge = document.getElementById('repl-badge');
    if (dot)   dot.dataset.state = state;
    if (badge) badge.textContent  = label;
  }

  /* Wire up the REPL panel controls. */
  const replPanel  = document.getElementById('repl-panel');
  const replToggle = document.getElementById('repl-toggle');

  if (replPanel && replToggle) {
    /* Show panel on toggle click. */
    replToggle.addEventListener('click', () => {
      const open = !replPanel.hidden;
      replPanel.hidden = open;
      replToggle.setAttribute('aria-expanded', String(!open));
      if (!open) {
        /* Start loading Pyodide the first time the user opens the REPL. */
        ensureReplPyodide();
        document.getElementById('repl-input').focus();
      }
    });

    /* Close button. */
    document.getElementById('repl-close-btn').addEventListener('click', () => {
      replPanel.hidden = true;
      replToggle.setAttribute('aria-expanded', 'false');
    });

    /* Clear button. */
    document.getElementById('repl-clear-btn').addEventListener('click', () => {
      document.getElementById('repl-output').innerHTML =
        '<span class="repl-output-placeholder">Output will appear here</span>';
      document.getElementById('repl-input').value = '';
    });

    /* Run button — compile and execute via Pyodide ProgramExecutor. */
    document.getElementById('repl-run-btn').addEventListener('click', async () => {
      const src    = document.getElementById('repl-input').value.trim();
      const lang   = document.getElementById('repl-lang').value;
      const output = document.getElementById('repl-output');
      if (!src) return;

      if (!_pyodideReady) {
        output.innerHTML = '<span class="repl-output-placeholder">Still loading — please wait…</span>';
        await ensureReplPyodide();
      }

      setReplStatus('running', 'running…');
      output.innerHTML = '<span class="repl-output-placeholder">Running…</span>';

      try {
        _pyodide.globals.set('_repl_code', src);
        _pyodide.globals.set('_repl_lang', lang);
        await _pyodide.runPythonAsync(`
from multilingualprogramming.codegen.executor import ProgramExecutor
_r        = ProgramExecutor(language=_repl_lang).execute(_repl_code)
_repl_out  = _r.output or ''
_repl_errs = '\\n'.join(_r.errors) if _r.errors else ''
`);
        renderOutput(output, {
          stdout: _pyodide.globals.get('_repl_out'),
          stderr: _pyodide.globals.get('_repl_errs'),
        });
        setReplStatus('ready', 'ready');
      } catch (err) {
        output.innerHTML = `<pre class="output-stderr">${err}</pre>`;
        setReplStatus('error', 'error');
      }
    });

    /* WAT button — generate WAT for the current user code via Pyodide. */
    document.getElementById('repl-wat-btn').addEventListener('click', async () => {
      const output = document.getElementById('repl-output');
      if (output.dataset.mode === 'wat') {
        output.innerHTML = '<span class="repl-output-placeholder">Output will appear here</span>';
        delete output.dataset.mode;
        return;
      }

      const src = document.getElementById('repl-input').value.trim();
      const lang = document.getElementById('repl-lang').value;

      output.innerHTML = '<span class="repl-output-placeholder">Generating WAT…</span>';
      output.dataset.mode = 'wat';

      if (!_pyodideReady) { await ensureReplPyodide(); }

      try {
        _pyodide.globals.set('_repl_code', src || '');
        _pyodide.globals.set('_repl_lang', lang);
        await _pyodide.runPythonAsync(`
from multilingualprogramming.lexer.lexer import Lexer
from multilingualprogramming.parser.parser import Parser
from multilingualprogramming.codegen.wat_generator import WATCodeGenerator
try:
  _toks    = Lexer(_repl_code, language=_repl_lang).tokenize()
  _prog    = Parser(_toks, source_language=_repl_lang).parse()
  _wat_out = WATCodeGenerator().generate(_prog)
  _wat_err = ''
except Exception as _e:
  _wat_out = ''
  _wat_err = str(_e)
`);
        const watSrc = _pyodide.globals.get('_wat_out');
        const watErr = _pyodide.globals.get('_wat_err');
        if (watErr) {
          output.innerHTML = `<pre class="output-stderr">${watErr}</pre>`;
          delete output.dataset.mode;
        } else {
          output.innerHTML = '';
          const pre = document.createElement('pre');
          pre.className = 'output-wat';
          pre.textContent = watSrc;
          output.appendChild(pre);
        }
      } catch (err) {
        output.innerHTML = `<pre class="output-stderr">${err}</pre>`;
        delete output.dataset.mode;
      }
    });

    /* Ctrl/Cmd+Enter to run. */
    document.getElementById('repl-input').addEventListener('keydown', e => {
      if (e.key === 'Enter' && (e.ctrlKey || e.metaKey)) {
        document.getElementById('repl-run-btn').click();
      }
    });
  }


  /* ================================================================
     RUN BUTTONS ON INLINE CODE BLOCKS
     Injected after the existing Copy button on every executable <pre>.
     ================================================================ */

  document.querySelectorAll('.content-body pre').forEach(pre => {
    const code = pre.querySelector('code');
    if (!code || !isExecutable(code)) return;
    if (code.classList.contains('language-python') && looksLikeHostPython(code.textContent || '')) return;

    /* Output panel inserted after <pre>. */
    const outputPanel = document.createElement('div');
    outputPanel.className = 'code-output';
    outputPanel.hidden = true;
    outputPanel.setAttribute('aria-live', 'polite');
    pre.insertAdjacentElement('afterend', outputPanel);

    /* Run button (sibling to existing Copy button inside <pre>). */
    const runBtn = document.createElement('button');
    runBtn.type      = 'button';
    runBtn.className = 'run-btn';
    runBtn.textContent = 'Run';
    runBtn.setAttribute('aria-label', 'Run this code');
    pre.appendChild(runBtn);

    runBtn.addEventListener('click', () => {
      const src    = code.textContent.trim();
      const hash16 = pre.dataset.blockHash || '';
      runBtn.textContent = '…';
      runBtn.disabled    = true;
      outputPanel.hidden = false;
      outputPanel.dataset.mode = 'output';
      outputPanel.innerHTML = '<span class="output-running">Running…</span>';

      /* hash16 is injected at build time by inject_hashes.py — no browser
       * hash computation needed. */
      MLWasm.execute(src, hash16)
        .then(result => {
          renderOutput(outputPanel, result);
        })
        .catch(err => {
          outputPanel.innerHTML = `<pre class="output-stderr">${err}</pre>`;
        })
        .finally(() => {
          runBtn.textContent = 'Run';
          runBtn.disabled    = false;
        });
    });

    /* View WAT button — shows the compiled WebAssembly text format. */
    const watBtn = document.createElement('button');
    watBtn.type      = 'button';
    watBtn.className = 'wat-btn';
    watBtn.textContent = 'WAT';
    watBtn.setAttribute('aria-label', 'View WebAssembly text format');
    pre.appendChild(watBtn);

    watBtn.addEventListener('click', () => {
      /* Toggle: if already showing WAT, hide the panel. */
      if (!outputPanel.hidden && outputPanel.dataset.mode === 'wat') {
        outputPanel.hidden = true;
        outputPanel.dataset.mode = '';
        return;
      }
      outputPanel.hidden = false;
      outputPanel.dataset.mode = 'wat';
      outputPanel.innerHTML = '<span class="output-running">Loading WAT…</span>';

      MLWasm.wat
        .then(text => {
          outputPanel.innerHTML = '';
          const pre = document.createElement('pre');
          pre.className = 'output-wat';
          pre.textContent = text;
          outputPanel.appendChild(pre);
        })
        .catch(() => {
          outputPanel.innerHTML =
            '<span class="output-stderr">WAT not available — run the CI build first.</span>';
        });
    });
  });

  /* ---- Mobile nav toggle ---- */
  const toggle = document.querySelector('.nav-toggle');
  const navLinks = document.querySelector('.nav-links');
  if (toggle && navLinks) {
    toggle.addEventListener('click', () => {
      const expanded = toggle.getAttribute('aria-expanded') === 'true';
      toggle.setAttribute('aria-expanded', String(!expanded));
      navLinks.classList.toggle('open');
    });
  }

  /* ---- TOC generation ---- */
  const toc = document.getElementById('toc');
  const article = document.querySelector('.content-body');
  if (toc && article) {
    const headings = article.querySelectorAll('h2, h3');
    if (headings.length > 0) {
      headings.forEach(h => {
        if (!h.id) {
          h.id = h.textContent.trim()
            .toLowerCase()
            .replace(/[^a-z0-9]+/g, '-')
            .replace(/^-|-$/g, '');
        }
        const a = document.createElement('a');
        a.href = '#' + h.id;
        a.textContent = h.textContent;
        a.className = h.tagName === 'H3' ? 'toc-h3' : '';
        toc.appendChild(a);
      });
    } else {
      toc.closest('.toc-panel').style.display = 'none';
    }
  }

  /* ---- Code tabs (demo on landing page) ---- */
  const tabs = document.querySelectorAll('.code-tab');
  tabs.forEach(tab => {
    tab.addEventListener('click', () => {
      const group = tab.closest('.code-demo');
      if (!group) return;
      const target = tab.dataset.target;
      group.querySelectorAll('.code-tab').forEach(t => t.classList.remove('active'));
      tab.classList.add('active');
      group.querySelectorAll('.code-panel').forEach(p => {
        p.style.display = p.dataset.lang === target ? 'block' : 'none';
      });
    });
  });

  /* ---- Active TOC highlighting on scroll ---- */
  if (toc) {
    const tocLinks = toc.querySelectorAll('a');
    const observer = new IntersectionObserver(entries => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          const id = entry.target.id;
          tocLinks.forEach(a => {
            a.classList.toggle('active', a.getAttribute('href') === '#' + id);
          });
        }
      });
    }, { rootMargin: '-20% 0px -70% 0px' });

    document.querySelectorAll('.content-body h2, .content-body h3').forEach(h => {
      if (h.id) observer.observe(h);
    });
  }

  /* ---- Copy code button ---- */
  document.querySelectorAll('.content-body pre').forEach(pre => {
    const btn = document.createElement('button');
    btn.className = 'copy-btn';
    btn.textContent = 'Copy';
    btn.setAttribute('aria-label', 'Copy code');
    pre.appendChild(btn);
    btn.addEventListener('click', () => {
      const code = pre.querySelector('code');
      if (code) {
        navigator.clipboard.writeText(code.textContent).then(() => {
          btn.textContent = 'Copied!';
          setTimeout(() => { btn.textContent = 'Copy'; }, 2000);
        });
      }
    });
  });

})();
