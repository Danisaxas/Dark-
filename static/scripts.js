function sendMessage() {
    let input = document.getElementById("user-input");
    let message = input.value.trim();
    if (message === "") return;

    let chatBox = document.getElementById("chat-box");
    chatBox.innerHTML += `<div class="user-message"><span>${message}</span></div>`;

    fetch("/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: message })
    })
    .then(response => response.json())
    .then(data => {
        chatBox.innerHTML += `<div class="bot-message"><span>${data.response}</span></div>`;
        input.value = "";
        chatBox.scrollTop = chatBox.scrollHeight;
    });
}

function handleKeyPress(event) {
    if (event.key === "Enter") {
        sendMessage();
    }
}
