const video = document.getElementById('background-video');

// Lắng nghe sự kiện timeupdate của video
video.addEventListener('timeupdate', () => {
    const duration = video.duration;

    // Kiểm tra nếu video chạy đến giây 19
    if (video.currentTime >= 19 && video.currentTime < 20) {
        document.body.style.backgroundImage = "url('background.png')"; // Thay nền bằng background.png
        video.pause(); // Dừng video khi đạt giây 19
    }
});

function backHome(){
    window.location.href = "/";
}
function goContact(){
    window.location.href = "/contact";
}

