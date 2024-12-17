fetch("/api/message")
    .then(response => response.json())
    .then(data => {
        document.getElementById("message").innerText = data.message;
    });

function nextPage(){
    window.location.href = "/tool";
}