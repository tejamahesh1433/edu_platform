// static/js/student_dashboard.js

document.addEventListener("DOMContentLoaded", function() {
    console.log("Student dashboard loaded");

    document.querySelector('.hamburger-menu').addEventListener('click', function() {
        document.querySelector('.sidebar').classList.toggle('active');
    });
});
