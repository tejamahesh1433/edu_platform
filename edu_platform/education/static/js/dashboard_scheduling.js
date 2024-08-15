// static/js/dashboard_scheduling.js

document.addEventListener("DOMContentLoaded", function() {
    console.log("Dashboard scheduling page loaded");

    // Toggle the sidebar
    document.querySelector('.hamburger-menu').addEventListener('click', function() {
        document.querySelector('.sidebar').classList.toggle('active');
    });

    // Placeholder for calendar initialization
    document.getElementById('calendar').innerHTML = 'Calendar will be displayed here...';

    // Load upcoming events (example data)
    const events = [
        { title: "Math Class", date: "2024-08-10", category: "class" },
        { title: "Science Project Deadline", date: "2024-08-12", category: "deadline" },
        { title: "Parent-Teacher Meeting", date: "2024-08-15", category: "meeting" }
    ];

    const eventList = document.getElementById('event-list');
    eventList.innerHTML = '';

    events.forEach(event => {
        const li = document.createElement('li');
        li.textContent = `${event.date}: ${event.title}`;
        li.classList.add(event.category);
        li.addEventListener('click', function() {
            openModal(event);
        });
        eventList.appendChild(li);
    });

    // Update event summary
    document.getElementById('total-events').textContent = events.length;
    document.getElementById('upcoming-events').textContent = events.length; // All are upcoming in this example
    document.getElementById('completed-events').textContent = 0; // Placeholder

    // Function to open the event details modal
    function openModal(event) {
        const modal = document.getElementById('event-modal');
        document.getElementById('modal-title').textContent = event.title;
        document.getElementById('modal-date').textContent = `Date: ${event.date}`;
        document.getElementById('modal-description').textContent = `Category: ${event.category}`;
        modal.style.display = "block";
    }

    // Function to close the event details modal
    document.querySelector('.close').addEventListener('click', closeModal);
    function closeModal() {
        document.getElementById('event-modal').style.display = "none";
    }

    // Functions for navigating dates
    document.getElementById('view-select').addEventListener('change', function() {
        // Logic to change calendar view (Day/Week/Month)
        alert(`Changed to ${this.value} view`);
    });

    window.prevDate = function() {
        alert('Navigate to the previous date');
    };

    window.nextDate = function() {
        alert('Navigate to the next date');
    };

    // Function to add a new event (placeholder)
    window.addEvent = function() {
        alert('Add new event functionality will be implemented here.');
    };
});
