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
function filterReports() {
    var reportType = document.getElementById('report-type').value;
    var reportDate = document.getElementById('report-date').value;

    // Apply the filters to the reports (example logic)
    console.log('Filtering reports:', reportType, reportDate);

    // Update the charts or data based on the selected filters
    document.getElementById('user-reports-chart').innerHTML = `Filtered user reports for ${reportType} on ${reportDate}`;
    document.getElementById('system-reports-chart').innerHTML = `Filtered system reports for ${reportType} on ${reportDate}`;
}

function exportReport(reportType) {
    // Export report logic (example)
    console.log('Exporting', reportType, 'report');
    alert(`${reportType.charAt(0).toUpperCase() + reportType.slice(1)} report exported successfully!`);
}
