const chatIcon = document.getElementById('chatIcon');
const chatWindow = document.getElementById('chatWindow');
const sendButton = document.getElementById('sendButton');
const chatInput = document.getElementById('chatInput');
const chatBody = document.getElementsByClassName('chat-body')[0];

chatIcon.addEventListener('click', () => {
    chatWindow.classList.toggle('chat-window-hidden');
    chatWindow.classList.toggle('chat-window-visible');
});

function addMessageToChat(message) {
    const messageElement = document.createElement('div');
    messageElement.innerText = message;
    messageElement.classList.add('chat-message');
    chatBody.appendChild(messageElement);
    chatBody.scrollTop = chatBody.scrollHeight;
}

sendButton.addEventListener('click', () => {
    if (chatInput.value.trim() !== '') {
        addMessageToChat(chatInput.value);
        chatInput.value = '';
    }
});

chatInput.addEventListener('keydown', (event) => {
    if (event.key === 'Enter') {
        if (chatInput.value.trim() !== '') {
            addMessageToChat(chatInput.value);
            chatInput.value = '';
        }
    }
});
