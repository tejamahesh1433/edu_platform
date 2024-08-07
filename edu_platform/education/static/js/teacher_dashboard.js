// static/js/teacher_dashboard.js

document.addEventListener("DOMContentLoaded", function() {
    console.log("Teacher dashboard loaded");

    document.querySelector('.hamburger-menu').addEventListener('click', function() {
        document.querySelector('.sidebar').classList.toggle('active');
    });
});
