document.addEventListener("DOMContentLoaded", () => {
    const menu_hamburger = document.querySelector(".hamburger input");
    const menu = document.querySelector(".menu");

    if (menu_hamburger && menu) {
        menu_hamburger.addEventListener("click", () => {
            // Verifica se o checkbox está marcado (ou seja, se o menu deve ser mostrado)
            if (menu_hamburger.checked) {
                // Mostra o menu com escala 1 (visível)
                menu.style.transform = "scale(1)";
            } else {
                // Oculta o menu com escala 0 (invisível)
                menu.style.transform = "scale(0)";
            }
        });
    }
});
