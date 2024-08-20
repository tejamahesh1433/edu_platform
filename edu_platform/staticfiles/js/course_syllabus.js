// course_syllabus.js

document.addEventListener("DOMContentLoaded", function() {
    // Any initialization code you might need
    console.log("Course Syllabus page is loaded");

    // Example of expanding and collapsing sections
    const sections = document.querySelectorAll('section h2');
    
    sections.forEach(section => {
        section.addEventListener('click', function() {
            const content = this.nextElementSibling;
            if (content.style.display === "none") {
                content.style.display = "block";
            } else {
                content.style.display = "none";
            }
        });
    });
});

// Example function for handling feedback form submissions
function submitFeedback(event) {
    event.preventDefault(); // Prevent the form from submitting in the traditional way
    const feedback = document.getElementById('feedback-text').value;
    alert(`Feedback submitted: ${feedback}`);
    // Here you could also send the feedback to a server using fetch or XMLHttpRequest
}

// Additional JS functions can be added as needed to manage interactivity on the page
