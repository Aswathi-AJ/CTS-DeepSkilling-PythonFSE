import { localCourses } from './data.js';

function logToUI(message, type = 'info') {
  console.log(`[HANDS-ON 4] ${message}`);
  const consoleBox = document.getElementById('console-output');
  if (consoleBox) {
    const entry = document.createElement('div');
    entry.className = `console-entry ${type}`;
    entry.textContent = `> ${message}`;
    consoleBox.appendChild(entry);
  }
}

export function fetchUserPromise(id) {
  return fetch(`https://jsonplaceholder.typicode.com/users/${id}`)
    .then(res => res.json())
    .then(user => {
      logToUI(`[Step 45] Promise User ${id}: ${user.name}`, 'info');
      return user.name;
    });
}

export async function fetchUserAsync(id) {
  try {
    const res = await fetch(`https://jsonplaceholder.typicode.com/users/${id}`);
    const user = await res.json();
    logToUI(`[Step 46] Async User ${id}: ${user.name}`, 'success');
    return user;
  } catch (err) {
    logToUI(`Error: ${err.message}`, 'warn');
  }
}

export function fetchAllCourses() {
  return new Promise(resolve => setTimeout(() => resolve(localCourses), 1000));
}
async function loadCourses() {
  const loading = document.getElementById('course-loading');
  const grid = document.getElementById('course-grid');
  const courses = await fetchAllCourses();
  loading.style.display = 'none';
  grid.innerHTML = courses.map(c => `
    <article class="course-card">
      <h3>${c.name}</h3>
      <p><strong>Code:</strong> ${c.code}</p>
      <div class="meta"><span>Credits: ${c.credits}</span><span class="badge">Grade: ${c.grade}</span></div>
    </article>
  `).join('');
  document.getElementById('total-credits').textContent = `Total Enrolled Credits: ${courses.reduce((a,b)=>a+b.credits,0)}`;
}

export async function apiFetch(url) {
  const res = await fetch(url);
  if (!res.ok) throw new Error(`API Error ${res.status}: ${res.statusText}`);
  return await res.json();
}

async function loadNotifications() {
  const posts = await apiFetch('https://jsonplaceholder.typicode.com/posts?_limit=4');
  document.getElementById('notifications-container').innerHTML = posts.map(p => `
    <div class="notification-card"><h4>📢 ${p.title}</h4><p>${p.body}</p></div>
  `).join('');
}

async function simulate404() {
  const errBox = document.getElementById('error-container');
  try {
    await apiFetch('https://jsonplaceholder.typicode.com/nonexistent_404');
  } catch (err) {
    errBox.innerHTML = `
      <div class="error-box">
        <p><strong>⚠️ Error:</strong> ${err.message}</p>
        <button id="retry-btn" class="btn-retry">🔄 Retry Request</button>
      </div>
    `;
    document.getElementById('retry-btn').addEventListener('click', simulate404);
  }
}

if (window.axios) {
  axios.interceptors.request.use(config => {
    logToUI(`[Axios Interceptor] Requesting: ${config.url}`, 'info');
    return config;
  });
}

document.addEventListener('DOMContentLoaded', () => {
  fetchUserPromise(1);
  fetchUserAsync(2);
  loadCourses();
  loadNotifications();
  simulate404();
});
