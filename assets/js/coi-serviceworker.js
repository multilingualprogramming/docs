/* coi-serviceworker.js
 * Injects Cross-Origin-Opener-Policy and Cross-Origin-Embedder-Policy headers
 * on every response so the page runs in a cross-origin isolated context.
 * This is required for SharedArrayBuffer and full WASM threading support on
 * GitHub Pages, which does not allow custom response headers.
 *
 * This file is dual-mode:
 *   - When executed as a <script> tag it registers itself as a Service Worker.
 *   - When executed as a Service Worker it intercepts fetches and adds headers.
 */

/* ---- Service Worker context -------------------------------------------- */
if (typeof window === 'undefined') {

  self.addEventListener('install', () => {
    self.skipWaiting();
  });

  self.addEventListener('activate', event => {
    event.waitUntil(self.clients.claim());
  });

  self.addEventListener('fetch', event => {
    /* Skip opaque cross-origin cache-only requests (avoids SW errors). */
    if (event.request.cache === 'only-if-cached' &&
        event.request.mode !== 'same-origin') {
      return;
    }

    event.respondWith(
      fetch(event.request).then(response => {
        /* Passthrough for opaque/error responses. */
        if (response.status === 0) return response;

        const headers = new Headers(response.headers);
        headers.set('Cross-Origin-Opener-Policy', 'same-origin');
        headers.set('Cross-Origin-Embedder-Policy', 'require-corp');

        return new Response(response.body, {
          status:     response.status,
          statusText: response.statusText,
          headers,
        });
      }).catch(() => fetch(event.request))
    );
  });

/* ---- Page context -------------------------------------------------------- */
} else {
  (async () => {
    /* Nothing to do if the page is already cross-origin isolated. */
    if (window.crossOriginIsolated) return;

    if (!('serviceWorker' in navigator)) {
      console.warn('[coi-sw] ServiceWorker not supported; WASM threads unavailable.');
      return;
    }

    /*
     * Derive the SW scope from the script's own URL so it works on both
     * local dev  (scope = "/")  and  GitHub Pages  (scope = "/docs/").
     *
     * Script URL:  https://…/docs/assets/js/coi-serviceworker.js
     * Scope:       https://…/docs/
     */
    const src   = document.currentScript.src;
    const scope = src.substring(0, src.indexOf('/assets/')) + '/';

    try {
      const reg = await navigator.serviceWorker.register(src, { scope });

      /*
       * On first install the SW is not yet controlling this page.
       * Wait for it to activate then reload once so headers take effect.
       */
      if (!navigator.serviceWorker.controller) {
        const sw = reg.installing || reg.waiting;
        if (sw) {
          await new Promise(resolve => {
            sw.addEventListener('statechange', function handler() {
              if (this.state === 'activated') {
                this.removeEventListener('statechange', handler);
                resolve();
              }
            });
          });
        }
        /* Single reload — after this the controller is active. */
        location.reload();
      }
    } catch (err) {
      console.warn('[coi-sw] Registration failed:', err);
    }
  })();
}
