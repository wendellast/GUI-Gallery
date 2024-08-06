
document.addEventListener('DOMContentLoaded', function() {
    const images = document.querySelectorAll('.image');

    images.forEach(image => {
        image.addEventListener('click', function(event) {
            event.stopPropagation();

            // Cria uma nova div de informações
            const infoPopup = document.createElement('div');
            infoPopup.className = 'info-popup';

            // Adiciona o texto e o botão de fechar
            const infoText = document.createElement('span');
            infoText.id = 'info-text';
            infoText.textContent = this.getAttribute('data-info');

            const closeBtn = document.createElement('button');
            closeBtn.className = 'close-btn';
            closeBtn.textContent = '×';

            infoPopup.appendChild(infoText);
            infoPopup.appendChild(closeBtn);

            // Adiciona a nova div ao corpo do documento
            document.body.appendChild(infoPopup);

            // Calcula a posição da popup
            const rect = this.getBoundingClientRect();
            const popupWidth = infoPopup.offsetWidth;
            const popupHeight = infoPopup.offsetHeight;

            let x = event.clientX;
            let y = event.clientY;

            // Ajusta a posição da popup para não sair da tela
            if (x + popupWidth > window.innerWidth) {
                x = window.innerWidth - popupWidth - 10;
            }
            if (y + popupHeight > window.innerHeight) {
                y = window.innerHeight - popupHeight - 10;
            }

            infoPopup.style.left = `${x}px`;
            infoPopup.style.top = `${y}px`;

            // Exibe a popup
            infoPopup.style.display = 'block';

            // Fecha a popup após 25 segundos
            const timer = setTimeout(() => {
                infoPopup.style.display = 'none';
                document.body.removeChild(infoPopup);
            }, 25000);

            // Fecha a popup quando o botão de fechar é clicado
            closeBtn.addEventListener('click', function() {
                clearTimeout(timer); // Cancela o fechamento automático
                infoPopup.style.display = 'none';
                document.body.removeChild(infoPopup);
            });
        });
    });

    // Para fechar a info-popup se clicar fora dela
    document.addEventListener('click', function(event) {
        const popups = document.querySelectorAll('.info-popup');
        popups.forEach(popup => {
            if (!popup.contains(event.target)) {
                popup.style.display = 'none';
                document.body.removeChild(popup);
            }
        });
    });
});

