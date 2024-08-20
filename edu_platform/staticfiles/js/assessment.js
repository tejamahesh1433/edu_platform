// Ensure DOM is fully loaded before executing scripts
document.addEventListener("DOMContentLoaded", function() {
    // Attach event listeners to form for submissions
    document.getElementById('assessmentForm').addEventListener('submit', handleFormSubmit);
    initializeEditButtons();
});

// Handle form submissions to add or update assessments
function handleFormSubmit(event) {
    event.preventDefault();
    const form = event.target;
    const data = {
        title: form.querySelector('#assessmentTitle').value,
        description: form.querySelector('#assessmentDescription').value
    };

    // Simulate API call with fetch (you'll replace this with your actual API URL)
    fetch('/api/assessments/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(assessment => {
        console.log('Success:', assessment);
        addAssessmentToTable(assessment);
        form.reset(); // Reset form fields after submission
    })
    .catch(error => console.error('Error:', error));
}

// Add a new row to the table with the assessment data
function addAssessmentToTable(assessment) {
    const table = document.getElementById('assessmentsTable').querySelector('tbody');
    const row = table.insertRow();
    row.innerHTML = `
        <td>${assessment.id}</td>
        <td>${assessment.title}</td>
        <td>${assessment.description}</td>
        <td>
            <button class="btn btn-secondary" onclick="editAssessment(${assessment.id})">Edit</button>
            <button class="btn btn-danger" onclick="deleteAssessment(${assessment.id}, this)">Delete</button>
        </td>
    `;
}

// Initialize edit and delete button event listeners
function initializeEditButtons() {
    const editButtons = document.querySelectorAll('.btn-secondary');
    editButtons.forEach(button => {
        button.addEventListener('click', () => editAssessment(button.dataset.id));
    });

    const deleteButtons = document.querySelectorAll('.btn-danger');
    deleteButtons.forEach(button => {
        button.addEventListener('click', () => deleteAssessment(button.dataset.id, button));
    });
}

// Edit assessment
function editAssessment(id) {
    console.log('Editing assessment', id);
    // Here you would fetch assessment details and populate the form to be edited
    // After fetching, you would show the modal window with the populated data
}

// Delete assessment
function deleteAssessment(id, button) {
    console.log('Deleting assessment', id);
    // Simulate API call to delete assessment
    fetch(`/api/assessments/${id}`, {
        method: 'DELETE'
    })
    .then(() => {
        // Remove the row from the table
        button.closest('tr').remove();
    })
    .catch(error => console.error('Error:', error));
}
