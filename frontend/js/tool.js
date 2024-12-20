
document.addEventListener("DOMContentLoaded", () => {
    const sendButton = document.getElementById("send-btn");
    const userMessage = document.getElementById("user-message");
    const responseText = document.getElementById("response-text");

    sendButton.addEventListener("click", async () => {
        const message = userMessage.value.trim();
        if (!message) {
            alert("Vui lòng nhập tin nhắn.");
            return;
        }

        try {
            // Gửi yêu cầu tới API backend
            const response = await fetch("/api/chat", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({ message })
            });

            if (!response.ok) {
                throw new Error("Có lỗi xảy ra khi gửi yêu cầu.");
            }

            const data = await response.json();
            responseText.textContent = data.reply;
        } catch (error) {
            responseText.textContent = "Có lỗi xảy ra: " + error.message;
        }
    });
});
