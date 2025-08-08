const countEl = document.getElementById('count');
const btn = document.getElementById('incBtn');

btn.addEventListener('click', () => {
  const current = parseInt(countEl.textContent, 10) || 0;
  countEl.textContent = current + 1;
});
