fetch("/api/message")
    .then(response => response.json())
    .then(data => {
        document.getElementById("message").innerText = data.message;
    });

// function nextPage(){
//     window.location.href = "/tool";
// }

const video = document.getElementById("background-video");
const contents = document.getElementById("contents");

// Ngừng phát video mặc định
video.pause();

function nextPage() {
    // Ẩn nội dung
    contents.style.display = "none";

    // Bắt đầu phát video
    video.play();

    const targetTime = 19; // Giây muốn video chạy đến trước khi chuyển trang
    const checkTime = () => {
        if (video.currentTime >= targetTime) {
            video.removeEventListener("timeupdate", checkTime); // Xóa sự kiện khi đã đạt thời gian
            window.location.href = "/tool"; // Chuyển trang
        }
    };

    // Theo dõi thời gian video
    video.addEventListener("timeupdate", checkTime);
}