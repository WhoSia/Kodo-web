(() => {
  const button = document.querySelector('[data-menu-button]');
  const mobileNav = document.querySelector('[data-mobile-nav]');
  const header = document.querySelector('[data-header]');

  const closeMenu = () => {
    if (!button || !mobileNav) return;
    button.setAttribute('aria-expanded', 'false');
    mobileNav.hidden = true;
    const mark = button.querySelector('.menu-mark');
    if (mark) mark.textContent = '+';
  };

  button?.addEventListener('click', () => {
    const open = button.getAttribute('aria-expanded') === 'true';
    button.setAttribute('aria-expanded', String(!open));
    mobileNav.hidden = open;
    const mark = button.querySelector('.menu-mark');
    if (mark) mark.textContent = open ? '+' : '−';
  });

  mobileNav?.querySelectorAll('a').forEach((link) => link.addEventListener('click', closeMenu));

  const syncHeader = () => header?.classList.toggle('is-scrolled', window.scrollY > 42);
  syncHeader();
  addEventListener('scroll', syncHeader, { passive: true });

  const media = window.KODO_MEDIA || {};
  document.querySelectorAll('[data-media-slot]').forEach((slot) => {
    const key = slot.getAttribute('data-media-slot');
    const item = media[key];
    if (!item || item.mode !== 'real' || !item.src || !item.alt) return;

    const img = slot.querySelector(`[data-real-media="${key}"]`);
    const caption = document.querySelector(`[data-media-caption="${key}"]`);
    const state = document.querySelector(`[data-media-state="${key}"]`);
    if (!img) return;

    const probe = new Image();
    probe.onload = () => {
      img.src = item.src;
      img.alt = item.alt;
      img.hidden = false;
      slot.classList.add('is-real');
      if (caption && item.caption) caption.textContent = item.caption;
      if (state) state.textContent = 'REAL PROJECT MEDIA';
    };
    probe.src = item.src;
  });

  const reducedMotion = matchMedia('(prefers-reduced-motion: reduce)').matches;
  if (!reducedMotion && 'IntersectionObserver' in window) {
    const observer = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (!entry.isIntersecting) return;
        entry.target.classList.add('is-visible');
        observer.unobserve(entry.target);
      });
    }, { threshold: 0.22 });
    document.querySelectorAll('[data-animate="figure"]').forEach((node) => observer.observe(node));
  } else {
    document.querySelectorAll('[data-animate="figure"]').forEach((node) => node.classList.add('is-visible'));
  }
})();
