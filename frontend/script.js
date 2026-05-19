const API_URL =
    "https://whatsapp-ai-agent-c60j.onrender.com/chat";


async function sendMessage() {

    const input = document.getElementById("message-input");

    const message = input.value;

    if (!message) return;

    addMessage("You", message, "user");

    input.value = "";

    const response = await fetch(API_URL, {
        method: "POST",

        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify({
            message: message
        })
    });

    const data = await response.json();

    addMessage(
        "AI",
        data.ai_response,
        "bot"
    );
}


function addMessage(sender, text, className) {

    const chatBox = document.getElementById("chat-box");

    const messageDiv = document.createElement("div");

    messageDiv.classList.add(
        "message",
        className
    );

    messageDiv.innerHTML =
        `<strong>${sender}:</strong> ${text}`;

    chatBox.appendChild(messageDiv);

    chatBox.scrollTop = chatBox.scrollHeight;
}