document.addEventListener('DOMContentLoaded', function() {
    const form = document.querySelector('form[action="{% url \'submit_feedback\' %}"]');
    
    form.addEventListener('submit', function(event) {
        if (!confirm('Are you sure you want to submit this feedback?')) {
            event.preventDefault(); // Prevent the form from being submitted
        }
    });
});
