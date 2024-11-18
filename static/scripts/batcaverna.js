document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("add-item-form");
    const trajesContainer = document.getElementById("trajes");
    const carrosContainer = document.getElementById("carros");
    const itensContainer = document.getElementById("itens");

    // Função para carregar itens
    async function loadItems() {
        try {
            const response = await fetch("/batcaverna/items", {
                method: "GET",
            });

            if (!response.ok) {
                throw new Error(`Erro ao carregar itens: ${response.status} - ${response.statusText}`);
            }

            const items = await response.json();

            // Limpa os containers
            trajesContainer.innerHTML = "";
            carrosContainer.innerHTML = "";
            itensContainer.innerHTML = "";

            // Adiciona os itens aos respectivos containers
            items.forEach((item) => {
                const itemDiv = document.createElement("div");
                itemDiv.classList.add("item");

                // Normaliza o caminho da imagem, substituindo barras invertidas por barras normais
                const imagePath = item.imagem.replace(/\\/g, "/");

                itemDiv.innerHTML = `
                    <img src="${imagePath}" alt="${item.nome}" />
                    <p>${item.nome} (${item.quantidade})</p>
                `;

                if (item.tipo === "traje") {
                    trajesContainer.appendChild(itemDiv);
                } else if (item.tipo === "carro") {
                    carrosContainer.appendChild(itemDiv);
                } else if (item.tipo === "item") {
                    itensContainer.appendChild(itemDiv);
                }
            });
        } catch (error) {
            console.error("Erro ao carregar itens:", error);
            alert("Erro ao carregar itens. Verifique o console para mais detalhes.");
        }
    }

    // Função para adicionar um novo item
    form.addEventListener("submit", async (event) => {
        event.preventDefault();

        const formData = new FormData(form);

        try {
            const response = await fetch("/batcaverna/items", {
                method: "POST",
                body: formData,
            });

            if (!response.ok) {
                throw new Error(`Erro ao adicionar item: ${response.status} - ${response.statusText}`);
            }

            const result = await response.json();
            alert(result.message);
            form.reset();
            loadItems();
        } catch (error) {
            console.error("Erro ao adicionar item:", error);
            alert("Erro ao adicionar item. Verifique o console para mais detalhes.");
        }
    });

    // Carregar os itens ao carregar a página
    loadItems();
});
