document.addEventListener("DOMContentLoaded", () => {
  document.querySelectorAll(".delete").forEach(button => {
    button.addEventListener("click", event => {
      if (!confirm("Delete this post permanently?")) event.preventDefault();
    });
  });
});
