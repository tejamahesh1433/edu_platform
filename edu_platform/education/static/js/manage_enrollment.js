// manage_enrollment.js

document.addEventListener("DOMContentLoaded", function() {
    // Event listener for adding students
    document.getElementById('add-student-btn').addEventListener('click', function() {
        let studentName = prompt("Enter the student's name:");
        if (studentName) {
            let studentList = document.getElementById('student-list');
            let li = document.createElement('li');
            li.textContent = studentName;
            let removeBtn = document.createElement('button');
            removeBtn.textContent = "Remove";
            removeBtn.className = "remove-btn";
            li.appendChild(removeBtn);
            studentList.appendChild(li);
        }
    });

    // Event delegation for removing students
    document.getElementById('student-list').addEventListener('click', function(e) {
        if (e.target && e.target.className === 'remove-btn') {
            e.target.parentElement.remove();
        }
    });
});
