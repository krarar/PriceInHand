const CACHE_NAME = 'modern-store-cache-v1';
const urlsToCache = [
  '/',
  '/index.html',
  '/styles.css',
  '/script.js',
  'https://firebasestorage.googleapis.com/v0/b/messageemeapp.appspot.com/o/PriceInHand-main%2F7da94f84-c767-466c-b0d3-b7bb852fd5e7.webp?alt=media&token=83c906f1-292a-4629-819b-3d137c911737'
];

self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then((cache) => cache.addAll(urlsToCache))
  );
});

self.addEventListener('fetch', (event) => {
  event.respondWith(
    caches.match(event.request)
      .then((response) => response || fetch(event.request))
  );
});