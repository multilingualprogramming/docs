/* Multilingual Docs - Main JS */
(function () {
  'use strict';

  /* ================================================================
     WASM MODULE LOADER
     Lazily instantiates assets/wasm/multilingual.wasm — the full
     multilingual interpreter compiled to WASM via Python + Cranelift
     (multilingualprogramming[wasm]).  No wasm-bindgen glue file.

     Expected binary exports:
       run_code(ptr: i32, len: i32) -> i32   source in, JSON result out
       __wasm_alloc(size: i32)       -> i32   linear-memory allocator
       __wasm_free(ptr: i32, size: i32)       linear-memory free
       memory                                 WebAssembly.Memory

     The loader resolves the base URL from the <meta name="base-url"> tag
     so paths work identically on local dev and under /docs on GitHub Pages.
     ================================================================ */

  const baseUrl = (document.querySelector('meta[name="base-url"]') || {}).content || '';

  const MLWasm = (() => {
    let _instance      = null;
    let _memory        = null;
    let _modulePromise = null;

    const enc = new TextEncoder();
    const dec = new TextDecoder();

    /* Instantiate the binary directly — no wasm-bindgen glue file needed.
     * The Cranelift-compiled binary exports:
     *   run_code(ptr: i32, len: i32) -> i32  (returns ptr to JSON result)
     *   __wasm_alloc(size: i32)       -> i32
     *   __wasm_free(ptr: i32, size: i32)
     *   memory                        (WebAssembly.Memory) */
    function load() {
      if (_modulePromise) return _modulePromise;

      const wasmUrl = baseUrl + '/assets/wasm/multilingual.wasm';

      _modulePromise = WebAssembly.instantiateStreaming(fetch(wasmUrl), {
        env: { abort: () => {} },
      }).then(({ instance }) => {
        _instance = instance;
        _memory   = instance.exports.memory;
        return true;
      });

      return _modulePromise;
    }

    /* Write a JS string into WASM linear memory; return { ptr, len }. */
    function writeStr(str) {
      const bytes = enc.encode(str);
      const ptr   = _instance.exports.__wasm_alloc(bytes.length + 1);
      const view  = new Uint8Array(_memory.buffer);
      view.set(bytes, ptr);
      view[ptr + bytes.length] = 0;
      return { ptr, len: bytes.length };
    }

    /* Read a null-terminated UTF-8 string from WASM linear memory. */
    function readStr(ptr) {
      const view = new Uint8Array(_memory.buffer);
      let end = ptr;
      while (view[end] !== 0) end++;
      return dec.decode(view.subarray(ptr, end));
    }

    /* ---- WAT text loader ------------------------------------------------- */
    /* Fetches the pre-generated .wat file (produced by wasm2wat in CI) once
     * and caches the text.  Used purely for display — execution always uses
     * the binary.  Returns Promise<string>. */
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

    /* Public API */
    return {
      /* Returns a Promise<{ stdout: string, stderr: string }>. */
      execute(src) {
        return load().then(() => {
          const { ptr, len } = writeStr(src);
          let resultPtr;
          try {
            resultPtr = _instance.exports.run_code(ptr, len);
          } finally {
            _instance.exports.__wasm_free(ptr, len + 1);
          }
          const raw = readStr(resultPtr);
          let out;
          try   { out = JSON.parse(raw); }
          catch { out = { stdout: raw, stderr: '' }; }
          return { stdout: out.stdout || '', stderr: out.stderr || '' };
        });
      },
      /* Expose the load promise so the toggle button can show readiness. */
      get ready() { return load(); },
      /* Returns a Promise<string> with the full WAT text. */
      get wat()   { return loadWat(); },
    };
  })();


  /* ================================================================
     REPL PANEL
     ================================================================ */

  /* Language classes that identify shell/config blocks — not executable
     multilingual source.  All other fenced blocks get a Run button. */
  const NON_EXECUTABLE = new Set([
    'language-bash', 'language-sh', 'language-shell',
    'language-powershell', 'language-cmd',
    'language-yaml', 'language-toml', 'language-json',
    'language-plaintext', 'language-text',
  ]);

  function isExecutable(codeEl) {
    return [...codeEl.classList].every(c => !NON_EXECUTABLE.has(c));
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

  /* Warm up the WASM module and update status indicators. */
  function initWasm() {
    MLWasm.ready
      .then(() => setReplStatus('ready', 'ready'))
      .catch(() => setReplStatus('error', 'unavailable'));
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
        /* Start loading WASM when the user first opens the REPL. */
        initWasm();
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

    /* Run button. */
    document.getElementById('repl-run-btn').addEventListener('click', () => {
      const src    = document.getElementById('repl-input').value.trim();
      const output = document.getElementById('repl-output');
      if (!src) return;

      setReplStatus('running', 'running…');
      output.innerHTML = '<span class="repl-output-placeholder">Running…</span>';

      MLWasm.execute(src)
        .then(result => {
          renderOutput(output, result);
          setReplStatus('ready', 'ready');
        })
        .catch(err => {
          output.innerHTML = `<pre class="output-stderr">${err}</pre>`;
          setReplStatus('error', 'error');
        });
    });

    /* WAT button — show compiled WebAssembly text in the output pane. */
    document.getElementById('repl-wat-btn').addEventListener('click', () => {
      const output = document.getElementById('repl-output');
      /* Toggle off if already showing WAT. */
      if (output.dataset.mode === 'wat') {
        output.innerHTML = '<span class="repl-output-placeholder">Output will appear here</span>';
        delete output.dataset.mode;
        return;
      }
      output.innerHTML = '<span class="repl-output-placeholder">Loading WAT…</span>';
      output.dataset.mode = 'wat';
      MLWasm.wat
        .then(text => {
          output.innerHTML = '';
          const pre = document.createElement('pre');
          pre.className = 'output-wat';
          pre.textContent = text;
          output.appendChild(pre);
        })
        .catch(() => {
          output.innerHTML =
            '<span class="output-stderr">WAT not available — build the WASM module first.</span>';
          delete output.dataset.mode;
        });
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
      const src = code.textContent.trim();
      runBtn.textContent = '…';
      runBtn.disabled    = true;
      outputPanel.hidden = false;
      outputPanel.dataset.mode = 'output';
      outputPanel.innerHTML = '<span class="output-running">Running…</span>';

      /* Load WASM lazily on first use. */
      MLWasm.execute(src)
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
