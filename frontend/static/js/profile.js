import { fetchUserProfile } from './api.js';

document.addEventListener('DOMContentLoaded', async () => {
  const container = document.getElementById('profile');
  const userId = 1; // static ID for demo
  const user = await fetchUserProfile(userId);

  if (user.username) {
    container.innerHTML = `
      <div class="p-4 border rounded bg-white">
        <img src="${user.avatar_url}" class="w-24 h-24 rounded-full mb-2">
        <h2 class="text-xl font-bold">${user.username}</h2>
        <p>${user.bio}</p>
      </div>
    `;
  } else {
    container.textContent = "User not found.";
  }
});