// app.js - Accessibility (a11y) & Keyboard Navigation Enhancements

document.addEventListener('DOMContentLoaded', () => {
  // Step 129: Keyboard accessibility for course cards
  const cards = document.querySelectorAll('.course-card');

  cards.forEach((card) => {
    // Listen for Enter or Space key press when focused
    card.addEventListener('keydown', (e) => {
      if (e.key === 'Enter' || e.key === ' ') {
        e.preventDefault();
        activateCard(card);
      }
    });

    // Also support mouse click
    card.addEventListener('click', () => {
      activateCard(card);
    });
  });

  function activateCard(card) {
    const isPressed = card.getAttribute('aria-pressed') === 'true';
    card.setAttribute('aria-pressed', (!isPressed).toString());
    card.classList.toggle('selected');
    
    // Step 130: Live region update
    const title = card.querySelector('h3').textContent;
    const statusBanner = document.getElementById('results-status');
    statusBanner.textContent = `Selected course: ${title}`;
  }

  // Step 130: Search live filter & announcement
  const searchInput = document.getElementById('course-search-input');
  const statusBanner = document.getElementById('results-status');

  searchInput.addEventListener('input', (e) => {
    const val = e.target.value.toLowerCase().trim();
    let count = 0;

    cards.forEach((card) => {
      const text = card.textContent.toLowerCase();
      if (text.includes(val)) {
        card.style.display = 'flex';
        count++;
      } else {
        card.style.display = 'none';
      }
    });

    // Announce match count to screen readers via aria-live
    statusBanner.textContent = `${count} accessible course${count === 1 ? '' : 's'} found for "${e.target.value}"`;
  });

  // Step 137: Trigger CSS variables ponyfill for cross-browser fallback
  if (window.cssVars) {
    cssVars({ watch: true });
  }
});
