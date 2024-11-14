function initializeLogin() {
    const loginForm = document.querySelector('#login-form');
    
    if (loginForm) {
        loginForm.addEventListener('submit', handleLogin);
    }
}

async function handleLogin(event) {
    event.preventDefault();
    
    const username = document.querySelector('#username').value;
    const password = document.querySelector('#password').value;

    try {

        const response = await fetch('http://localhost:5000/login', { 
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ username, senha: password })
        });

        if (!response.ok) {
            throw new Error(`Erro: ${response.status} - ${response.statusText}`);
        }

        const result = await response.json();
        alert(result.message);

        if (response.ok) {
            alert('Login realizado com sucesso!');
            // Redirecionar ou executar outra ação
            // window.location.href = '/dashboard'; 
        }
    } catch (error) {
        console.error('Erro ao fazer login:', error);
        alert('Erro ao fazer login: ' + error.message);
    }
}

document.addEventListener('DOMContentLoaded', initializeLogin);
