document.addEventListener("DOMContentLoaded", () => {
    const loginForm = document.getElementById("login-form");

    loginForm.addEventListener("submit", async (event) => {
        event.preventDefault();

        const username = document.getElementById("username").value;
        const password = document.getElementById("password").value;

        try {
            const response = await fetch("/login", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({ username, senha: password }),
            });

            const result = await response.json();

            if (response.ok) {
                localStorage.setItem("role", result.role || "user");
                localStorage.setItem("username", result.username || "Usuário");
                window.location.href = `/main?role=${result.role}&username=${result.username}`;
            } else {
                alert(result.message);
            }
        } catch (error) {
            console.error("Erro ao fazer login:", error);
            alert("Erro ao fazer login. Tente novamente.");
        }
    });
});
