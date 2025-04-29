document.addEventListener('DOMContentLoaded', () => {
    // Get modal elements
    const loginModal = document.getElementById('login-modal');
    const signupModal = document.getElementById('signup-modal');
    const loginBtn = document.getElementById('login-btn');
    const signupBtn = document.getElementById('signup-btn');
    const closeButtons = document.querySelectorAll('.modal-close');
    const switchToSignup = document.getElementById('switch-to-signup');
    const switchToLogin = document.getElementById('switch-to-login');

    // Functions to show/hide modals
    const showModal = (modal) => {
        modal.classList.add('active');
        document.body.style.overflow = 'hidden';
    };

    const hideModal = (modal) => {
        modal.classList.remove('active');
        document.body.style.overflow = '';
    };

    // Event listeners for opening modals
    loginBtn?.addEventListener('click', (e) => {
        e.preventDefault();
        showModal(loginModal);
    });

    signupBtn?.addEventListener('click', (e) => {
        e.preventDefault();
        showModal(signupModal);
    });

    // Event listeners for closing modals
    closeButtons.forEach(button => {
        button.addEventListener('click', () => {
            hideModal(loginModal);
            hideModal(signupModal);
        });
    });

    // Event listeners for switching between modals
    switchToSignup?.addEventListener('click', (e) => {
        e.preventDefault();
        hideModal(loginModal);
        showModal(signupModal);
    });

    switchToLogin?.addEventListener('click', (e) => {
        e.preventDefault();
        hideModal(signupModal);
        showModal(loginModal);
    });

    // Close modal when clicking outside
    window.addEventListener('click', (e) => {
        if (e.target.classList.contains('modal-overlay')) {
            hideModal(e.target);
        }
    });

    // Close modal on escape key
    document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape') {
            hideModal(loginModal);
            hideModal(signupModal);
        }
    });
}); 