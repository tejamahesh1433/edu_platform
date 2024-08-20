document.addEventListener('DOMContentLoaded', function () {
    // Example: Highlighting the row when clicking
    const rows = document.querySelectorAll('tbody tr');

    rows.forEach(row => {
        row.addEventListener('click', function () {
            rows.forEach(r => r.classList.remove('highlight'));
            this.classList.add('highlight');
        });
    });
});

