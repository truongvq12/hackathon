function navigateTo(page) {
    window.location.href = `/${page}`;
}

function backHome() {
    window.location.href = "/";
}

function goContact() {
    window.location.href = "/contact";
}

// Function to toggle the sidebar (open or close)
function toggleSidebar() {
    const sidebar = document.querySelector('.sidebar');
    sidebar.classList.toggle('close');
}

// Giữ sidebar mở mặc định khi tải trang
document.addEventListener('DOMContentLoaded', function() {
    const sidebar = document.querySelector('.sidebar');
    sidebar.classList.add('open'); // Đảm bảo sidebar luôn mở khi tải trang
});
