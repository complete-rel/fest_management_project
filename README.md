/**
 * Jazz Fest 2025 - Event Management System
 * 
 * Full-stack event management system designed to streamline the organization of jazz festivals.
 * Backend: Django (API with DRF, ORM, Authentication, Slug-based URLs)
 * Frontend: React
 */

const projectOverview = {
  name: "Jazz Fest 2025",
  description: "A full-stack event management system for jazz festivals.",
  backend: "Django with DRF",
  frontend: "React",
  features: {
    backend: [
      "Event Management",
      "Venue Management",
      "Ticketing System",
      "Volunteer Management",
      "Slug-based URLs",
      "User Authentication",
      "Database Models (Django ORM)",
      "API Development (DRF)"
    ],
    frontend: [
      "Dynamic UI with React",
      "Event Listings",
      "Venue Information",
      "Authentication System",
      "Ticket Purchasing"
    ]
  }
};

const projectStructure = `
fest_management_project/
│── backend/
│   ├── fest_management/
│   ├── venues/
│   ├── events/
│   ├── tickets/
│   ├── volunteers/
│   ├── users/
│   ├── db.sqlite3
│   ├── virt/  # Virtual environment
│── frontend/
│   ├── src/
│   │   ├── api/
│   │   ├── components/
│   ├── node_modules/
│   ├── tsconfig.json
│── README.md
`;

const apiEndpoints = [
  { endpoint: "/api/events/", method: "GET", description: "Retrieve all events" },
  { endpoint: "/api/events/<slug>/", method: "GET", description: "Retrieve a specific event" },
  { endpoint: "/api/venues/", method: "GET", description: "Retrieve all venues" },
  { endpoint: "/api/venues/<slug>/", method: "GET", description: "Retrieve a specific venue" },
  { endpoint: "/api/tickets/", method: "GET", description: "Retrieve all tickets" },
  { endpoint: "/api/volunteers/", method: "GET", description: "Retrieve all volunteer opportunities" },
  { endpoint: "/api/users/register/", method: "POST", description: "User registration" },
  { endpoint: "/api/users/login/", method: "POST", description: "User login" }
];

console.log("Project Overview:", projectOverview);
console.log("Project Structure:", projectStructure);
console.log("API Endpoints:", apiEndpoints);

/**
 * Installation Steps:
 * 
 * Backend:
 * 1. git clone https://github.com/complete_rel/fest_management_project.git
 * 2. cd fest_management_project/backend
 * 3. python -m venv virt
 * 4. source virt/bin/activate  (Windows: virt\Scripts\activate)
 * 5. pip install -r requirements.txt
 * 6. python manage.py migrate
 * 7. python manage.py runserver
 * 
 * Frontend:
 * 1. cd ../frontend
 * 2. npm install
 * 3. npm start
 */

export { projectOverview, projectStructure, apiEndpoints };
