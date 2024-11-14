function openModal(image) {
  const modal = document.getElementById('imageModal');
  const modalImage = modal.querySelector('#modalImage');
  
  modal.setAttribute('aria-hidden', 'false');  // Muestra el modal
  modalImage.src = image.src;
}

function closeModal() {
  const modal = document.getElementById('imageModal');
  modal.setAttribute('aria-hidden', 'true');  // Oculta el modal
}

// Asegúrate de que el modal esté oculto al cargar la página
window.onload = function() {
  closeModal();
};
