document.getElementById('sendButton').addEventListener('click', function() {
    const userInput = document.getElementById('userInput').value;
    const chatBox = document.getElementById('chatBox');

    if (userInput.trim() !== "") {
        const userMessage = document.createElement('div');
        userMessage.textContent = "You: " + userInput;
        chatBox.appendChild(userMessage);

        document.getElementById('userInput').value = '';

        // Simulate bot response
        setTimeout(() => {
            const botMessage = document.createElement('div');
            botMessage.textContent = "Bot: " + getBotResponse(userInput);
            chatBox.appendChild(botMessage);

            chatBox.scrollTop = chatBox.scrollHeight;
        }, 1000);
    }
});

function getBotResponse(input) {
    // Simple keyword-based responses
    input = input.toLowerCase();
    if (input.includes("안녕")) {
        return "안녕하세요! 무엇을 도와드릴까요?";
    } else if (input.includes("우울증")) {
        return "우울증 자가진단 페이지로 접속합니다.";
    } else if (input.includes("치매")) {
        return "치매 자가진단 페이지로 접속합니다.";
    } else if (input.includes("ADHD")) {
        return "ADHD 자가진단 페이지로 접속합니다.";
    } else if (input.includes("bye")) {
        return "Goodbye! Have a great day!";
    } else if (input.includes("bye")) {
        return "Goodbye! Have a great day!";
    } else if (input.includes("bye")) {
        return "Goodbye! Have a great day!";
    } else {
        return "I'm sorry, I don't understand. Can you rephrase?";
    }
}
