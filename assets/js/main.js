/* Multilingual Docs - Main JS */
(function () {
  'use strict';

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
