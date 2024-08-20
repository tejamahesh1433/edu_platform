// Initialization of charts when the document is ready
document.addEventListener("DOMContentLoaded", function() {
    initializeCharts();
    loadCourseCompletionChart(); // Pre-load data for course completion on start
});

// Define chart variables globally to reference for updates
let userActivityChart, courseCompletionChart, engagementChart, financialMetricsChart, feedbackAnalysisChart;

function initializeCharts() {
    // Initialize static charts or placeholders
    initUserActivityChart();
    initEngagementChart();
    initFinancialMetricsChart();
    initFeedbackAnalysisChart();
}

// Fetch and dynamically update the course completion chart
function loadCourseCompletionChart() {
    fetch('/api/course-data/')
        .then(response => response.json())
        .then(data => {
            updateCourseCompletionChart(data.labels, data.completion_rates);
        })
        .catch(error => console.error('Error loading course data:', error));
}

function initUserActivityChart() {
    const ctx = document.getElementById('userActivityChart').getContext('2d');
    userActivityChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: ['January', 'February', 'March', 'April'],
            datasets: [{
                label: 'Daily Active Users',
                data: [120, 190, 300, 450],
                backgroundColor: 'rgba(255, 99, 132, 0.2)',
                borderColor: 'rgba(255, 99, 132, 1)',
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
}

function updateCourseCompletionChart(labels, data) {
    const ctx = document.getElementById('courseCompletionChart').getContext('2d');
    if (courseCompletionChart) {
        courseCompletionChart.destroy(); // Destroy the existing chart if it exists
    }
    courseCompletionChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: labels,
            datasets: [{
                label: 'Completion Rate',
                data: data,
                backgroundColor: 'rgba(54, 162, 235, 0.6)',
                borderColor: 'rgba(54, 162, 235, 1)',
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                y: {
                    beginAtZero: true,
                    ticks: {
                        callback: function(value) { return value + "%" }
                    }
                }
            },
            responsive: true,
            maintainAspectRatio: false
        }
    });
}

// Initialize other charts similarly, add update functions if needed
function initEngagementChart() {
    const ctx = document.getElementById('engagementChart').getContext('2d');
    engagementChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: ['Week 1', 'Week 2', 'Week 3', 'Week 4'],
            datasets: [{
                label: 'User Engagements',
                data: [200, 240, 270, 300],
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
}

// Initialize Financial Metrics Chart
function initFinancialMetricsChart() {
    const ctx = document.getElementById('financialMetricsChart').getContext('2d');
    financialMetricsChart = new Chart(ctx, {
        type: 'pie',
        data: {
            labels: ['Revenue', 'Expenses', 'Profit'],
            datasets: [{
                label: 'Financial Overview',
                data: [30000, 20000, 10000],
                backgroundColor: [
                    'rgba(153, 102, 255, 0.6)',
                    'rgba(255, 159, 64, 0.6)',
                    'rgba(255, 205, 86, 0.6)'
                ],
                borderColor: [
                    'rgba(153, 102, 255, 1)',
                    'rgba(255, 159, 64, 1)',
                    'rgba(255, 205, 86, 1)'
                ],
                borderWidth: 1
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false
        }
    });
}

// Fetch and dynamically update the financial metrics chart
function loadFinancialMetricsChart() {
    fetch('/api/financial-data/')
        .then(response => response.json())
        .then(data => {
            updateFinancialMetricsChart(data.labels, data.values);
        })
        .catch(error => console.error('Error loading financial metrics data:', error));
}

function updateFinancialMetricsChart(labels, data) {
    if (financialMetricsChart) {
        financialMetricsChart.data.labels = labels;
        financialMetricsChart.data.datasets[0].data = data;
        financialMetricsChart.update();
    }
}

// Initialize Feedback Analysis Chart
function initFeedbackAnalysisChart() {
    const ctx = document.getElementById('feedbackAnalysisChart').getContext('2d');
    feedbackAnalysisChart = new Chart(ctx, {
        type: 'radar',
        data: {
            labels: ['Responsiveness', 'Content Quality', 'Usability', 'Feature Richness'],
            datasets: [{
                label: 'User Feedback Scores',
                data: [65, 59, 90, 81],
                backgroundColor: 'rgba(255, 99, 132, 0.5)',
                borderColor: 'rgba(255, 99, 132, 1)',
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                r: {
                    angleLines: {
                        display: false
                    },
                    suggestedMin: 50,
                    suggestedMax: 100
                }
            },
            responsive: true,
            maintainAspectRatio: false
        }
    });
}

// Fetch and dynamically update the feedback analysis chart
function loadFeedbackAnalysisChart() {
    fetch('/api/feedback-data/')
        .then(response => response.json())
        .then(data => {
            updateFeedbackAnalysisChart(data.labels, data.scores);
        })
        .catch(error => console.error('Error loading feedback data:', error));
}

function updateFeedbackAnalysisChart(labels, scores) {
    if (feedbackAnalysisChart) {
        feedbackAnalysisChart.data.labels = labels;
        feedbackAnalysisChart.data.datasets[0].data = scores;
        feedbackAnalysisChart.update();
    }
}
