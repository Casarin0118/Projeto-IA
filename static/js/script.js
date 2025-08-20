document.addEventListener('DOMContentLoaded', () => {

    const loginFormContainer = document.getElementById('login-form');
    const registerFormContainer = document.getElementById('register-form');
    const showRegisterLink = document.getElementById('show-register');
    const showLoginLink = document.getElementById('show-login');

    showRegisterLink.addEventListener('click', (event) => {
        event.preventDefault();
        loginFormContainer.classList.add('hidden');
        registerFormContainer.classList.remove('hidden');
    });

    showLoginLink.addEventListener('click', (event) => {
        event.preventDefault();
        loginFormContainer.classList.remove('hidden');
        registerFormContainer.classList.add('hidden');
    });

    const loginForm = document.getElementById('login-form-element');
    const registerForm = document.getElementById('register-form-element');

    const handleFormSubmit = (event) => {
        event.preventDefault();

        const form = event.target;
        const formData = new FormData(form);
        const url = form.action;

        fetch(url, {
            method: 'POST',
            body: formData,
        })
        .then(response => response.json())
        .then(data => {
            alert(data.message);
            form.reset();
        })
        .catch(error => {
            console.error('Ocorreu um erro:', error);
            alert('Não foi possível conectar ao servidor.');
        });
    };

    loginForm.addEventListener('submit', handleFormSubmit);
    registerForm.addEventListener('submit', handleFormSubmit);

});