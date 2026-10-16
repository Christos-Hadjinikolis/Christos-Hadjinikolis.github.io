/* Cal.com embed bootstrap, adapted from packages/embeds/embed-snippet/src/index.ts. */
(function (C, A, L) {
  const push = function (api, args) { api.q.push(args); };
  C.Cal = C.Cal || function () {
    const cal = C.Cal;
    const args = arguments;
    if (!cal.loaded) {
      cal.ns = {};
      cal.q = cal.q || [];
      C.document.head.appendChild(C.document.createElement('script')).src = A;
      cal.loaded = true;
    }
    if (args[0] === L) {
      const api = function () { push(api, arguments); };
      const namespace = args[1];
      api.q = api.q || [];
      if (typeof namespace === 'string') {
        cal.ns[namespace] = cal.ns[namespace] || api;
        push(cal.ns[namespace], args);
        push(cal, ['initNamespace', namespace]);
      } else push(cal, args);
      return;
    }
    push(cal, args);
  };
})(window, 'https://app.cal.com/embed/embed.js', 'init');

window.Cal('init', 'catch-up', { origin: 'https://cal.com' });
window.Cal.ns['catch-up']('inline', {
  elementOrSelector: '#catch-up-calendar',
  calLink: 'christos-hadjinikolis-htrxr6/30min',
  config: { layout: 'month_view', theme: 'light' }
});
window.Cal.ns['catch-up']('ui', { theme: 'light', layout: 'month_view', hideEventTypeDetails: false });

const copyButton = document.getElementById('copy-link');
const shareUrl = document.getElementById('share-url');
const copyStatus = document.getElementById('copy-status');
copyButton.hidden = false;
copyButton.addEventListener('click', async function () {
  try {
    await navigator.clipboard.writeText(shareUrl.value);
    copyStatus.textContent = 'Link copied.';
  } catch (error) {
    shareUrl.focus();
    shareUrl.select();
    copyStatus.textContent = 'Select and copy the link above.';
  }
});
