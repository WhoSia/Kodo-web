const fs = require('node:fs');
const assert = require('node:assert/strict');
const { chromium } = require('playwright');

// Pin a working source baseline; compare the same DOM at identical viewport/theme.
const BASELINE = process.env.KODO_BASELINE_CSS || '/tmp/kodo-css-baseline.css';
const SITE = process.env.KODO_TEST_URL || 'http://127.0.0.1:4173';
const css = fs.readFileSync(BASELINE, 'utf8');
const widths = [1440, 720, 390];
const props = [
  'display','position','visibility','opacity','color','backgroundColor',
  'borderTopWidth','borderRightWidth','borderBottomWidth','borderLeftWidth',
  'borderTopColor','borderRightColor','borderBottomColor','borderLeftColor',
  'borderRadius','boxShadow','outlineStyle','outlineWidth','outlineColor',
  'fontFamily','fontSize','fontWeight','lineHeight','letterSpacing',
  'marginTop','marginRight','marginBottom','marginLeft',
  'paddingTop','paddingRight','paddingBottom','paddingLeft',
  'width','height','minWidth','maxWidth','minHeight','maxHeight',
  'gridTemplateColumns','gridTemplateRows','gap','rowGap','columnGap',
  'flexDirection','flexWrap','alignItems','justifyContent',
  'transform','filter','objectFit','overflowX','overflowY','zIndex',
];
function fingerprint(props) {
  return [...document.querySelectorAll('body, body *')].map((el, index) => {
    const cssValue = getComputedStyle(el);
    const box = el.getBoundingClientRect();
    const values = Object.fromEntries(props.map(p => [p, cssValue[p]]));
    return {
      index,
      tag: el.tagName,
      class: el.className?.baseVal ?? el.className,
      id: el.id,
      bounds: [box.x,box.y,box.width,box.height].map(n => Math.round(n * 100) / 100),
      values,
    };
  });
}
(async () => {
  const browser = await chromium.launch();
  try {
    for (const width of widths) for (const theme of ['dark','light']) {
      async function capture(baseline) {
        const context = await browser.newContext({ viewport: { width, height: 900 }, reducedMotion: 'reduce' });
        try {
          if (theme === 'light') {
            await context.addInitScript(() => localStorage.setItem('kodo-theme-v0112', 'light'));
          }
          const page = await context.newPage();
          if (baseline) {
            await page.route('**/styles.css', route => route.fulfill({
              status: 200, contentType: 'text/css; charset=utf-8', body: css,
            }));
          }
          await page.goto(SITE, { waitUntil: 'load' });
          await page.evaluate(() => document.fonts.ready);
          return await page.evaluate(fingerprint, props);
        } finally {
          await context.close();
        }
      }
      const before = await capture(true);
      const after = await capture(false);
      assert.equal(after.length, before.length, 'DOM count changed');
      for (let i = 0; i < after.length; i++) {
        assert.deepEqual(after[i], before[i],
          'computed-style/layout drift at width=' + width + ', theme=' + theme +
          ', element=' + i + ', id=' + after[i]?.id + ', class=' + after[i]?.class);
      }
      console.log('CSS_PARITY=PASS width=' + width + ' theme=' + theme + ' elements=' + after.length);
    }
  } finally { await browser.close(); }
})().catch(e => { console.error('CSS_PARITY=FAIL', e); process.exitCode = 1; });
