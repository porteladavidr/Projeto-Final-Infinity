document.addEventListener("DOMContentLoaded", () => {
    const role = localStorage.getItem("role") || "user";
    const username = localStorage.getItem("username") || "Usuário";
    const restrictedButton = document.getElementById("restricted-access");
    const restrictedResources = document.getElementById("resources")
    const userInfo = document.getElementById("user-info");

    userInfo.textContent = `Usuário: ${username}`;

    if (role !== "admin") {
        restrictedButton.disabled = true;
        restrictedButton.title = "Acesso restrito a administradores.";
    }

    restrictedButton.addEventListener("click", () => {
        if (role === "admin") {
            window.location.href = `/batcaverna?role=${role}`;
        }
    });

    if (role !== "admin" && role !== "gerente" ) {
        restrictedResources.disabled = true;
        restrictedResources.title = "Acesso restrito a administradores.";
    }

    restrictedResources.addEventListener("click", () => {
        if (role === "admin" || role === "gerente") {
            window.location.href = `/gestao?role=${role}`;
        }
    });

    const logoutButton = document.getElementById("logout");
    logoutButton.addEventListener("click", () => {
        localStorage.clear();
        window.location.href = "/";
    });
});
