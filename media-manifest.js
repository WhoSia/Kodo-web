/*
  Media truth gate.
  Keep mode="conceptual" until a real, publishable Kodo capture is approved.
  To replace the hero fallback, add the file under assets/ and set mode="real".
*/
const KODO_MEDIA_CANONICAL = {
  hero: {
    mode: "conceptual",
    src: "",
    alt: "",
    caption: "Environment structure and agent-state system view."
  }
};

window.KODO_MEDIA_PROVIDER = {
  resolve(mode = window.KODO_MEDIA_MODE) {
    if (mode === 'preview' && window.KODO_MEDIA_PREVIEW) return window.KODO_MEDIA_PREVIEW;
    return KODO_MEDIA_CANONICAL;
  }
};
Object.defineProperty(window, 'KODO_MEDIA', {
  configurable: true,
  get: () => window.KODO_MEDIA_PROVIDER.resolve()
});
window.KODO_RESOLVE_MEDIA = () => window.KODO_MEDIA_PROVIDER.resolve();
