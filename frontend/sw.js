const CACHE_NAME = "aprendelab-v31";
const STATIC_ASSETS = [
  "/",
  "/index.html",
  "/manifest.json",
  "/icon.svg",
  "/css/styles.css",
  "/js/icons.js",
  "/js/art.js",
  "/js/math_render.js",
  "/js/tools_drawer.js",
  "/js/diagrams.js",
  "/js/main.js",
  "/js/views/dashboard.js",
  "/js/views/library.js",
  "/js/views/settings.js",
  "/js/views/roadmap.js",
  "/js/views/learn.js",
  "/js/views/review.js",
  "/js/views/session.js",
  "/js/views/creator.js",
  "/js/views/exercises.js",
  "/js/views/ingreso.js",
  "/js/views/study_hub.js",
  "/js/views/diagnostic.js",
  "/js/labs/guitar_lab.js",
  "/js/labs/electronics_lab.js",
  "/js/labs/math_lab.js",
  "/js/labs/physics_lab.js"
];

self.addEventListener("install", (event) => {
  event.waitUntil(
    caches.open(CACHE_NAME).then((cache) => cache.addAll(STATIC_ASSETS)).catch(() => {})
  );
  self.skipWaiting();
});

self.addEventListener("activate", (event) => {
  event.waitUntil(
    caches.keys().then((keys) =>
      Promise.all(keys.filter((k) => k !== CACHE_NAME).map((k) => caches.delete(k)))
    )
  );
  self.clients.claim();
});

self.addEventListener("fetch", (event) => {
  const url = new URL(event.request.url);
  if (url.pathname.startsWith("/api/") || event.request.method !== "GET") {
    return;
  }
  event.respondWith(
    fetch(event.request)
      .then((res) => {
        const clone = res.clone();
        caches.open(CACHE_NAME).then((cache) => cache.put(event.request, clone)).catch(() => {});
        return res;
      })
      .catch(() => caches.match(event.request))
  );
});
