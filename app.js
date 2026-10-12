"use strict";
// Shared client-side enhancements. Server-side validation remains authoritative.
document.addEventListener("DOMContentLoaded", () => {
  document.querySelectorAll('input[type="number"]').forEach((input) => {
    input.addEventListener("input", () => input.setCustomValidity(""));
  });
  document.querySelectorAll("form").forEach((form) => {
    form.addEventListener("submit", () => {
      const button = form.querySelector('button[type="submit"], button:not([type])');
      if (button && form.checkValidity()) {
        button.dataset.originalText = button.textContent;
        button.textContent = "Processing...";
        button.disabled = true;
      }
    });
  });
});
