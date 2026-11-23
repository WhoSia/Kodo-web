(() => {
  const root = document.documentElement;
  const button = document.querySelector('[data-menu-button]');
  const mobileNav = document.querySelector('[data-mobile-nav]');
  const header = document.querySelector('[data-header]');
  const themeButton = document.querySelector('[data-theme-toggle]');
  const themeLabel = document.querySelector('[data-theme-label]');
  const themeColor = document.querySelector('[data-theme-color]');
  const THEME_KEY = 'kodo-theme-v0112';

  const applyTheme = (theme, persist = true) => {
    const next = theme === 'light' ? 'light' : 'dark';
    root.dataset.theme = next;
    if (themeLabel) themeLabel.textContent = next === 'dark' ? 'Light' : 'Dark';
    if (themeButton) themeButton.setAttribute('aria-label', `Switch to ${next === 'dark' ? 'light' : 'dark'} theme`);
    if (themeColor) themeColor.setAttribute('content', next === 'dark' ? '#070a0f' : '#efe8da');
    if (persist) {
      try { localStorage.setItem(THEME_KEY, next); } catch (_) {}
    }
  };

  let initialTheme = 'dark';
  try { initialTheme = localStorage.getItem(THEME_KEY) || 'dark'; } catch (_) {}
  applyTheme(initialTheme, false);
  themeButton?.addEventListener('click', () => applyTheme(root.dataset.theme === 'dark' ? 'light' : 'dark'));

  const closeMenu = ({ restoreFocus = false } = {}) => {
    if (!button || !mobileNav) return;
    button.setAttribute('aria-expanded', 'false');
    mobileNav.hidden = true;
    const mark = button.querySelector('.menu-mark');
    if (mark) mark.textContent = '+';
    if (restoreFocus) button.focus();
  };

  button?.addEventListener('click', () => {
    const open = button.getAttribute('aria-expanded') === 'true';
    button.setAttribute('aria-expanded', String(!open));
    mobileNav.hidden = open;
    const mark = button.querySelector('.menu-mark');
    if (mark) mark.textContent = open ? '+' : '−';
  });

  mobileNav?.querySelectorAll('a').forEach((link) => link.addEventListener('click', () => closeMenu()));
  document.addEventListener('keydown', (event) => {
    if (event.key === 'Escape' && button?.getAttribute('aria-expanded') === 'true') {
      closeMenu({ restoreFocus: true });
    }
  });
  document.addEventListener('pointerdown', (event) => {
    if (button?.getAttribute('aria-expanded') !== 'true') return;
    if (!header?.contains(event.target)) closeMenu();
  });
  const desktop = matchMedia('(min-width: 721px)');
  desktop.addEventListener('change', (event) => { if (event.matches) closeMenu(); });

  const syncHeader = () => header?.classList.toggle('is-scrolled', window.scrollY > 42);
  syncHeader();
  addEventListener('scroll', syncHeader, { passive: true });


})();
