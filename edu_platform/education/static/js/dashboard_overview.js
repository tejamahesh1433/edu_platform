// static/js/dashboard_overview.js

document.addEventListener("DOMContentLoaded", function() {
    console.log("dashboard overview page loaded");

    document.querySelector('.hamburger-menu').addEventListener('click', function() {
        document.querySelector('.sidebar').classList.toggle('active');
    });

    // Example chart code (you can replace this with actual chart library code)
    document.getElementById('engagement-chart').innerHTML = 'Engagement chart goes here...';
    document.getElementById('performance-chart').innerHTML = 'Performance chart goes here...';
});
