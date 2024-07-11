document.addEventListener('DOMContentLoaded', () => {
    const hamburger = document.querySelector('.hamburger');
    const navLinks = document.querySelector('.nav-links');
    const menuItems = document.querySelectorAll('.nav-links a');

    hamburger.addEventListener('click', () => {
        toggleMenu();
    });

    menuItems.forEach(item => {
        item.addEventListener('click', () => {
            if (navLinks.classList.contains('active')) {
                toggleMenu();
            }
        });
    });

    function toggleMenu() {
        navLinks.classList.toggle('active');
        hamburger.classList.toggle('active');
    }
});
function startTimer(duration, display) {
    var timer = duration, minutes, seconds;
    var resendBtn = document.getElementById('resend-otp-btn');
    var interval = setInterval(function () {
        minutes = parseInt(timer / 60, 10);
        seconds = parseInt(timer % 60, 10);
        minutes = minutes < 10 ? "0" + minutes : minutes;
        seconds = seconds < 10 ? "0" + seconds : seconds;
        display.textContent = "OTP will expire in: " + minutes + ":" + seconds;
        if (--timer < 0) {
            clearInterval(interval);
            display.textContent = "OTP expired!";
            resendBtn.style.display = "inline";
        }
    }, 1000);
}
window.onload = function () {
    var twoMinutes = 60 * 2,
        display = document.getElementById('otp-timer');
    startTimer(twoMinutes, display);
};
