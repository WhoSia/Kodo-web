const { chromium } = require('playwright');
const assert = require('node:assert/strict');
const fs = require('node:fs');

const origin = process.env.KODO_TEST_URL || 'http://127.0.0.1:4173';
const screenshotDir = process.env.KODO_SCREENSHOT_DIR;
if (screenshotDir) fs.mkdirSync(screenshotDir, { recursive: true });
const sizes = [
  { width: 1440, height: 900 },
  { width: 1024, height: 900 },
  { width: 820, height: 900 },
  { width: 721, height: 900 },
  { width: 720, height: 900 },
  { width: 390, height: 844 },
  { width: 360, height: 780 },
];
(async () => {
  const browser = await chromium.launch({ headless: true });
  try {
    for (const viewport of sizes) {
      const context = await browser.newContext({ viewport, reducedMotion: 'reduce' });
      const page = await context.newPage();
      const errors = [];
      const badAssets = [];
      page.on('pageerror', error => errors.push(error.message));
      page.on('response', response => {
        const url = new URL(response.url());
        if (url.origin === new URL(origin).origin && response.status() >= 400) {
          badAssets.push(url.pathname + ': ' + response.status());
        }
      });
      await page.goto(origin, { waitUntil: 'load', timeout: 30000 });
      await page.locator('h1').waitFor();
      assert.equal(await page.locator('html').getAttribute('data-theme'), 'dark', 'dark default');
      assert.equal(await page.locator('.roadmap-stop').count(), 5, 'five stages');
      assert.equal(await page.locator('.menu-mark').count(), 1, 'menu mark exists');

      const metrics = await page.evaluate(() => ({
        scroll: document.documentElement.scrollWidth,
        viewport: document.documentElement.clientWidth,
        css: getComputedStyle(document.body).backgroundColor,
      }));
      assert(metrics.scroll <= metrics.viewport + 2, 'horizontal overflow at ' + viewport.width + ': ' + JSON.stringify(metrics));
      assert.notEqual(metrics.css, 'rgba(0, 0, 0, 0)', 'nontransparent body background');
      assert.equal(await page.locator('.perception-panel').count(), 4, 'four perception panels');
      assert.equal(await page.locator('.reality-steps article').count(), 3, 'three field conditions');
      assert.equal(await page.locator('link[rel="stylesheet"]').count(), 1, 'one CSS entry');

      const logoOk = await page.locator('.brand-lockup img').evaluateAll(nodes =>
        nodes.every(n => n.complete && n.naturalWidth > 0));
      assert(logoOk, 'header logo assets load');

      await page.locator('[data-theme-toggle]').click();
      assert.equal(await page.locator('html').getAttribute('data-theme'), 'light', 'theme toggle');
      await page.reload({ waitUntil: 'domcontentloaded' });
      assert.equal(await page.locator('html').getAttribute('data-theme'), 'light', 'theme persistence');
      if (screenshotDir) await page.screenshot({
        path: screenshotDir + '/kodo-' + viewport.width + '-light.png', fullPage: true,
        animations: 'disabled',
      });
      await page.locator('[data-theme-toggle]').click();
      assert.equal(await page.locator('html').getAttribute('data-theme'), 'dark', 'dark restore');
      if (viewport.width >= 721) {
        assert.equal(await page.locator('.desktop-nav').isVisible(), true, 'desktop nav at ' + viewport.width);
        assert.equal(await page.locator('[data-menu-button]').isVisible(), false, 'mobile menu button hidden at desktop width');
      }
      if (viewport.width < 721) {
        const button = page.locator('[data-menu-button]');
        const nav = page.locator('[data-mobile-nav]');
        assert.equal(await nav.isVisible(), false, 'mobile nav initially hidden');
        await button.click();
        assert.equal(await button.getAttribute('aria-expanded'), 'true', 'expanded on open');
        assert.equal(await page.locator('.menu-mark').textContent(), '−', 'menu mark open');
        assert.equal(await nav.isVisible(), true, 'mobile nav visible');
        await page.keyboard.press('Escape');
        assert.equal(await nav.isVisible(), false, 'Escape closes');
        assert.equal(await page.locator('.menu-mark').textContent(), '+', 'menu mark reset');
        assert.equal(await button.evaluate(n => document.activeElement === n), true, 'Escape restores focus');
        await button.click();
        await page.locator('.hero h1').click();
        assert.equal(await nav.isVisible(), false, 'outside interaction closes');
        await button.click();
        await page.locator('[data-mobile-nav] a').first().click();
        assert.equal(await nav.isVisible(), false, 'nav action closes');
      }
      assert.deepEqual(errors, [], 'page JS errors');
      assert.deepEqual(badAssets, [], 'broken same-origin HTTP requests');
      if (screenshotDir) await page.screenshot({
        path: screenshotDir + '/kodo-' + viewport.width + '-dark.png', fullPage: true,
        animations: 'disabled',
      });
      console.log('BROWSER_GATE=PASS viewport=' + viewport.width);
      await context.close();
    }
  } finally {
    await browser.close();
  }
})().catch(error => { console.error('BROWSER_GATE=FAIL', error); process.exitCode = 1; });
