# Jazz Fest 2025 - Event Management System

## Project Overview 

Jazz Fest 2025 is a full-stack event management system designed to streamline the organization of jazz festivals.

- **Backend**: Django with DRF (Django REST Framework) for API development, ORM for database management, authentication, and slug-based URLs.
    
- **Frontend**: React for a dynamic user experience.
    

## Features

### Backend

- Event Management
    
- Venue Management
    
- Ticketing System
    
- Volunteer Management
    
- Slug-based URLs for clean routing
    
- User Authentication
    
- Database Models (Django ORM)
    
- API Development using DRF
    

### Frontend

- Dynamic UI with React
    
- Event Listings
    
- Venue Information
    
- User Authentication
    
- Ticket Purchasing
    

## Project Structure

```
fest_management_project/
│── backend/
│   ├── fest_management/
│   ├── venues/
│   ├── events/
│   ├── tickets/
│   ├── volunteers/
│   ├── users/
│   ├── db.sqlite3  
│   ├── virt/  
│── frontend/
│   ├── src/
│   │   ├── api/
│   │   ├── components/
│   ├── node_modules/
│   ├── tsconfig.json
│── README.md
```

## API Endpoints

|Endpoint|Method|Description|
|---|---|---|
|`/api/events/`|GET|Retrieve all events|
|`/api/events/<slug>/`|GET|Retrieve a specific event|
|`/api/venues/`|GET|Retrieve all venues|
|`/api/venues/<slug>/`|GET|Retrieve a specific venue|
|`/api/tickets/`|GET|Retrieve all tickets|
|`/api/volunteers/`|GET|Retrieve all volunteer opportunities|
|`/api/users/register/`|POST|User registration|
|`/api/users/login/`|POST|User login|

## Installation Steps

### Backend

1. Clone the repository:
    
    ```
    git clone https://github.com/complete_rel/fest_management_project.git
    ```
    
2. Navigate to the backend folder:
    
    ```
    cd fest_management_project/backend
    ```
    
3. Create a virtual environment and activate it:
    
    ```
    python -m venv virt
    source virt/bin/activate  # On Windows: virt\Scripts\activate
    ```
    
4. Install dependencies:
    
    ```
    pip install -r requirements.txt
    ```
    
5. Run database migrations:
    
    ```
    python manage.py migrate
    ```
    
6. Start the development server:
    
    ```
    python manage.py runserver
    ```
    

### Frontend

1. Navigate to the frontend folder:
    
    ```
    cd ../frontend
    ```
    
2. Install dependencies:
    
    ```
    npm install
    ```
    
3. Start the development server:
    
    ```
    npm start
    ```
    

## Contributing

If you'd like to contribute, feel free to submit a pull request or open an issue.

## License

This project is licensed under the MIT License.

---

**Author**: Complete_rel  
**GitHub**: [complete_rel](https://github.com/complete_rel)
