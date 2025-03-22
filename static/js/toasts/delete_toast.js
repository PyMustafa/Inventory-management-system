document.addEventListener('DOMContentLoaded', function () {
  const toastContainer = document.getElementById('toastContainer');
  const toastTemplate = document.getElementById('toastTemplate');
  let toastCounter = 0;


  document.getElementById('addToastBtn').addEventListener('click', function () {
    toastCounter++;


    const newToast = toastTemplate.cloneNode(true);
    newToast.id = `toast-${toastCounter}`; // Assign a unique ID
    newToast.style.display = 'block'; // Make it visible

    const toastHeader = newToast.querySelector('.toast-header strong');
    const toastBody = newToast.querySelector('.toast-body p');
    toastHeader.textContent = "Delete record";
    toastBody.textContent = "You are deleted this record";


    toastContainer.appendChild(newToast);

    // Initialize and show the Bootstrap toast
    const bsToast = new bootstrap.Toast(newToast);
    bsToast.show();


    newToast.addEventListener('hidden.bs.toast', function () {
      newToast.remove();
    });
  });

});