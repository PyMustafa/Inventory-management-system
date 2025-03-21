document.addEventListener('DOMContentLoaded', function () {
  const toastContainer = document.getElementById('toastContainer');
  const toastTemplate = document.getElementById('toastTemplate');
  let toastCounter = 0;


  document.getElementById('addToastBtn').addEventListener('click', function () {
    toastCounter++;


    const newToast = toastTemplate.cloneNode(true);
    newToast.id = `toast-${toastCounter}`;
    newToast.style.display = 'block';


    const toastHeader = newToast.querySelector('.toast-header strong');
    const toastBody = newToast.querySelector('.toast-body p');


    toastBody.innerHTML = `
      <span style="
        background-color: #28a745;
        color: white;
        padding: 5px 8px;
        border-radius: 50%;
        margin-right: 10px;
      ">
        <i class="fas fa-check"></i>
      </span>
      The record has been added successfully.
    `;

    toastContainer.appendChild(newToast);

    const bsToast = new bootstrap.Toast(newToast);
    bsToast.show();
  });
});


