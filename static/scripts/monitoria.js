document.addEventListener("DOMContentLoaded", async () => {
    const monitors = [
        document.getElementById("monitor1"),
        document.getElementById("monitor2"),
        document.getElementById("monitor3"),
        document.getElementById("monitor4"),
    ];

    const images = [
        "/static/img/monitor/1.jpg",
        "/static/img/monitor/2.jpg",
        "/static/img/monitor/3.jpg",
        "/static/img/monitor/4.jpg",
        "/static/img/monitor/5.jpg",
        "/static/img/monitor/6.jpg",
        "/static/img/monitor/7.jpg",
        "/static/img/monitor/8.jpg",
        "/static/img/monitor/9.jpg",
    ];

    let imageIndex = 0;

    async function loadCameras() {
        try {
            // Fazer requisição para obter o estado das câmeras
            const response = await fetch("/gestao/cameras");
            if (!response.ok) {
                throw new Error("Erro ao carregar dados das câmeras.");
            }
            const cameras = await response.json();

            // Atualizar os monitores apenas com câmeras ativas
            monitors.forEach((monitor, index) => {
                monitor.innerHTML = ""; // Limpa o monitor

                const camera = cameras.find(cam => cam.id === index + 1); // Localizar câmera correspondente
                if (camera && camera.ativa) {
                    const imgElement = document.createElement("img");
                    imgElement.src = images[imageIndex % images.length]; // Ciclo infinito de imagens
                    monitor.appendChild(imgElement);
                    imageIndex++;
                }
            });
        } catch (error) {
            console.error(error);
            alert("Erro ao carregar o monitoramento. Verifique o console.");
        }
    }

    // Atualizar monitores periodicamente (refresh a cada 5 segundos)
    setInterval(loadCameras, 5000);

    // Carregar as câmeras no início
    loadCameras();
});
