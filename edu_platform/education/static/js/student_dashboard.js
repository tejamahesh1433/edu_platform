// JavaScript for toggling the sidebar menu
function toggleSidebar() {
    document.body.classList.toggle('open-sidebar');
}

// Function to load personalized content in the feed section
function loadPersonalizedFeed() {
    // Example: Fetch personalized feed content via AJAX
    fetch('/api/personalized_feed/')
        .then(response => response.json())
        .then(data => {
            const feed = document.getElementById('feed');
            feed.innerHTML = ''; // Clear existing content
            data.forEach(item => {
                const div = document.createElement('div');
                div.className = 'feed-item';
                div.innerHTML = `<h3>${item.title}</h3><p>${item.content}</p>`;
                feed.appendChild(div);
            });
        })
        .catch(error => console.error('Error fetching personalized feed:', error));
}

// Function to load progress visualization
function loadProgressVisualization() {
    // Example: Fetch progress data via AJAX and render chart
    fetch('/api/progress_visualization/')
        .then(response => response.json())
        .then(data => {
            const progressVisualization = document.getElementById('progressVisualization');
            // Assuming we're using a library like Chart.js to render charts
            new Chart(progressVisualization, {
                type: 'bar',
                data: {
                    labels: data.labels,
                    datasets: [{
                        label: 'Course Progress',
                        data: data.progress,
                        backgroundColor: 'rgba(75, 192, 192, 0.2)',
                        borderColor: 'rgba(75, 192, 192, 1)',
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
        .catch(error => console.error('Error fetching progress visualization:', error));
}

// Initialize functions on page load
document.addEventListener('DOMContentLoaded', function() {
    loadPersonalizedFeed();
    loadProgressVisualization();
});
