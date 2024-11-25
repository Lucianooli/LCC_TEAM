document.addEventListener("DOMContentLoaded", function () {
    // Verifica se o usuário já viu a tela de carregamento
    if (!localStorage.getItem("hasVisited")) {
        // Espera 3 segundos para remover a tela de carregamento
        setTimeout(function () {
          // Remove a tela de carregamento
          document.getElementById('loading-screen').style.display = 'none';
          // Mostra o conteúdo do site
          document.getElementById('content').style.display = 'block';
        }, 5000);

        // Marca que o usuário já viu a tela de carregamento
        localStorage.setItem("hasVisited", "true");
    } else {
        // Se o usuário já visitou, apenas mostra o conteúdo
        document.getElementById('loading-screen').style.display = 'none';
        document.getElementById('content').style.display = 'block';
    }
});
