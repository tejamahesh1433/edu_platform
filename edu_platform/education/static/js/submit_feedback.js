document.getElementById('feedbackForm').addEventListener('submit', function(event) {
    var confirmation = confirm('Are you sure you want to submit this feedback?');
    if (!confirmation) {
        event.preventDefault(); // Prevent form submission if the user cancels
    }
});
