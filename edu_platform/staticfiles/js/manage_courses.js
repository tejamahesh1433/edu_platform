// static/js/manage_courses.js

document.addEventListener("DOMContentLoaded", function() {
    console.log("Manage courses page loaded");
    // Add any additional JavaScript functionality here if needed
});

document.addEventListener('DOMContentLoaded', function () {
    // Confirm before deleting a course
    const deleteLinks = document.querySelectorAll('a[href*="delete_course"]');
    deleteLinks.forEach(function (link) {
        link.addEventListener('click', function (event) {
            const confirmDelete = confirm('Are you sure you want to delete this course? This action cannot be undone.');
            if (!confirmDelete) {
                event.preventDefault();
            }
        });
    });
});
