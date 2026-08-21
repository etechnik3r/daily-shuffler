/*
 * Service Worker for Daily Taktgeber.
 *
 * Responsibilities:
 *   1. Offline capability – the app shell is precached on install so the tool
 *      works with no network. Cache-first serving keeps it instant.
 *   2. Cache housekeeping – on activation every cache whose name does not match
 *      the current CACHE_NAME is deleted, so bumping CACHE_VERSION cleans up
 *      all previous versions automatically.
 *   3. Controlled updates – this worker deliberately does NOT call skipWaiting()
 *      on install. It stays in "waiting" so the page can show an update banner;
 *      only when the user opts in (a SKIP_WAITING message) does it take over.
 *
 * IMPORTANT: bump CACHE_VERSION on every release. A changed CACHE_VERSION
 * changes the bytes of this file, which is what makes the browser register a
 * new worker → triggers the in-app "new version available" banner.
 */
const CACHE_VERSION = 'v9';
const CACHE_NAME = `daily-taktgeber-${CACHE_VERSION}`;

// Same-origin core assets that make up the offline app shell.
const CORE_ASSETS = [
  'daily_timer.html',
  'manifest.webmanifest',
  'icons/icon-192.png',
  'icons/icon-512.png',
  'icons/icon-maskable-512.png',
  'icons/apple-touch-icon.png',
];

self.addEventListener('install', (event) => {
  event.waitUntil((async () => {
    const cache = await caches.open(CACHE_NAME);
    // {cache:'reload'} bypasses the HTTP cache so we always precache fresh files.
    await cache.addAll(CORE_ASSETS.map((url) => new Request(url, { cache: 'reload' })));
    // No skipWaiting() here: wait until the user accepts the update.
  })());
});

self.addEventListener('activate', (event) => {
  event.waitUntil((async () => {
    // Remove every cache from a previous CACHE_VERSION.
    const keys = await caches.keys();
    await Promise.all(
      keys.filter((key) => key !== CACHE_NAME).map((key) => caches.delete(key))
    );
    await self.clients.claim();
  })());
});

// Let the page tell a waiting worker to activate immediately.
self.addEventListener('message', (event) => {
  if (event.data && event.data.type === 'SKIP_WAITING') {
    self.skipWaiting();
  }
});

self.addEventListener('fetch', (event) => {
  const req = event.request;
  if (req.method !== 'GET') return;

  const url = new URL(req.url);

  // Navigations always resolve to the app shell (cache-first, network fallback).
  if (req.mode === 'navigate') {
    event.respondWith((async () => {
      const cached = await caches.match('daily_timer.html');
      if (cached) return cached;
      try {
        return await fetch(req);
      } catch (e) {
        return (await caches.match('daily_timer.html')) || Response.error();
      }
    })());
    return;
  }

  if (url.origin === self.location.origin) {
    // Same-origin assets: serve from cache, fall back to network and cache it.
    event.respondWith((async () => {
      const cached = await caches.match(req);
      if (cached) return cached;
      try {
        const res = await fetch(req);
        if (res && res.ok) {
          const copy = res.clone();
          const cache = await caches.open(CACHE_NAME);
          cache.put(req, copy);
        }
        return res;
      } catch (e) {
        return Response.error();
      }
    })());
    return;
  }

  // Cross-origin (e.g. web fonts): try the network, fall back to any cached copy.
  event.respondWith(fetch(req).catch(() => caches.match(req)));
});
