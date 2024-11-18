document.addEventListener("DOMContentLoaded", async () => {
    const form = document.getElementById("camera-form");

    // Carregar estado inicial das câmeras
    async function loadCameras() {
        try {
            const response = await fetch("/gestao/cameras");
            if (!response.ok) {
                throw new Error("Erro ao carregar câmeras.");
            }
            const cameras = await response.json();
            cameras.forEach(camera => {
                const checkbox = document.querySelector(`#camera${camera.id}`);
                if (checkbox) {
                    checkbox.checked = camera.ativa;
                }
            });
        } catch (error) {
            console.error(error);
            alert("Erro ao carregar câmeras. Verifique o console.");
        }
    }

    // Salvar estado das câmeras
    form.addEventListener("submit", async (event) => {
        event.preventDefault();
        const data = Array.from(form.querySelectorAll("input[type=checkbox]")).map(input => ({
            id: input.dataset.id,
            ativa: input.checked
        }));

        try {
            const response = await fetch("/gestao/cameras", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify(data)
            });
            if (!response.ok) {
                throw new Error("Erro ao salvar configurações.");
            }
            alert("Configurações salvas com sucesso!");
        } catch (error) {
            console.error(error);
            alert("Erro ao salvar configurações. Verifique o console.");
        }
    });

    // Carregar estado inicial
    loadCameras();
});
