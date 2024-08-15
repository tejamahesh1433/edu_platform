// static/js/adaptive_learning.js

document.addEventListener("DOMContentLoaded", function() {
    console.log("Adaptive learning page loaded");

    document.querySelector('.hamburger-menu').addEventListener('click', function() {
        document.querySelector('.sidebar').classList.toggle('active');
    });

    // Example chart code (you can replace this with actual chart library code)
    document.getElementById('engagement-chart').innerHTML = 'Engagement chart goes here...';
    document.getElementById('performance-chart').innerHTML = 'Performance chart goes here...';
});
