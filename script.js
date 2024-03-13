document.addEventListener('DOMContentLoaded', function() {
    const contactSellerButton = document.querySelector('.inquiry-button');
    const sellerModal = document.getElementById('sellerModal');
    const modalOverlay = document.getElementById('modalOverlay');

    contactSellerButton.addEventListener('click', function() {
        sellerModal.style.display = 'block';
    });

    modalOverlay.addEventListener('click', function() {
        sellerModal.style.display = 'none';
    });
});