// JavaScript for toggling the sidebar menu
function toggleSidebar() {
    document.body.classList.toggle('open-sidebar');
}

// Function to load notifications
function loadNotifications() {
    // Example: Fetch notifications via AJAX
    fetch('/api/notifications/')
        .then(response => response.json())
        .then(data => {
            const notifications = document.querySelector('.notifications');
            notifications.innerHTML = ''; // Clear existing content
            data.forEach(notification => {
                const div = document.createElement('div');
                div.className = 'notification-item';
                div.innerHTML = `<p>${notification.message}</p><small>${notification.timestamp}</small>`;
                notifications.appendChild(div);
            });
        })
        .catch(error => console.error('Error fetching notifications:', error));
}

// Function to load student engagement metrics
function loadEngagementMetrics() {
    // Example: Fetch engagement metrics via AJAX and render chart
    fetch('/api/engagement_metrics/')
        .then(response => response.json())
        .then(data => {
            const engagementCharts = document.getElementById('engagementCharts');
            // Assuming we're using a library like Chart.js to render charts
            new Chart(engagementCharts, {
                type: 'line',
                data: {
                    labels: data.labels,
                    datasets: [{
                        label: 'Student Engagement',
                        data: data.engagement,
                        backgroundColor: 'rgba(153, 102, 255, 0.2)',
                        borderColor: 'rgba(153, 102, 255, 1)',
                        borderWidth: 1
                    }]
                },
                options: {
                    scales: {
                        y: {
                            beginAtZero: true
                        }
                    }
                }
            });
        })
        .catch(error => console.error('Error fetching engagement metrics:', error));
}

// Initialize functions on page load
document.addEventListener('DOMContentLoaded', function() {
    loadNotifications();
    loadEngagementMetrics();
});
