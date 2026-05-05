function ask(question) {
    document.getElementById('userInput').value = question;
    sendMessage();
}

async function sendMessage() {
    const input = document.getElementById('userInput');
    const messages = document.getElementById('messages');
    const sendBtn = document.getElementById('sendBtn');
    const message = input.value.trim();

    if (!message) return;

    // Mensaje del usuario
    messages.innerHTML += `
        <div class="message user">
            <div class="bubble">${message}</div>
        </div>
    `;

    input.value = '';
    sendBtn.disabled = true;
    sendBtn.textContent = 'Enviando...';

    // Indicador de escritura
    messages.innerHTML += `
        <div class="message bot" id="typing">
            <div class="bubble">✍️ Pensando...</div>
        </div>
    `;

    messages.scrollTop = messages.scrollHeight;

    try {
        const response = await fetch('/chat/message', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ message })
        });

        const data = await response.json();

        // Reemplazar indicador por respuesta
        document.getElementById('typing').outerHTML = `
            <div class="message bot">
                <div class="bubble">${data.response}</div>
            </div>
        `;
    } catch (error) {
        document.getElementById('typing').outerHTML = `
            <div class="message bot">
                <div class="bubble">❌ Error al conectar con la IA. Revisá la API key.</div>
            </div>
        `;
    }

    sendBtn.disabled = false;
    sendBtn.textContent = 'Enviar';
    messages.scrollTop = messages.scrollHeight;
}

// Enviar con Enter
document.getElementById('userInput').addEventListener('keypress', function(e) {
    if (e.key === 'Enter') sendMessage();
});