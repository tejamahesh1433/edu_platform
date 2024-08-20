// static/js/dashboard_insights.js

document.addEventListener("DOMContentLoaded", function() {
    console.log("Dashboard insights page loaded");

    document.querySelector('.hamburger-menu').addEventListener('click', function() {
        document.querySelector('.sidebar').classList.toggle('active');
    });

    // Example chart code (you can replace this with actual chart library code)
    document.getElementById('engagement-chart').innerHTML = 'Engagement chart goes here...';
    document.getElementById('performance-chart').innerHTML = 'Performance chart goes here...';
});
