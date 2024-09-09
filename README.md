Fitness Center Management System
Overview
This is a Flask-based web application designed to manage members and workout sessions at a fitness center. The application uses Flask-SQLAlchemy to interact with a database and provides RESTful APIs for CRUD (Create, Read, Update, Delete) operations.

Features
Member Management:
Create new members
Retrieve all members
Update existing members
Delete members
Workout Session Management:
Create new workout sessions
Retrieve all workout sessions
Retrieve a workout session by ID
Update existing workout sessions
Delete workout sessions
Requirements
Python 3.8+
Flask 2.0+
Flask-SQLAlchemy 2.5+
SQLite (or any other database supported by Flask-SQLAlchemy)
Installation
Clone the repository: git clone https://github.com/cececodes1/fitness_center_project.git
Install dependencies: pip install -r requirements.txt
Create a new database: flask db init
Apply migrations: flask db migrate and flask db upgrade
Usage
Run the application: flask run
Use a tool like Postman or cURL to interact with the APIs
API Endpoints
Member Endpoints
POST /members: Create a new member
GET /members: Retrieve all members
GET /members/<id>: Retrieve a member by ID
PUT /members/<id>: Update an existing member
DELETE /members/<id>: Delete a member
Workout Session Endpoints
POST /workout-sessions: Create a new workout session
GET /workout-sessions: Retrieve all workout sessions
GET /workout-sessions/<id>: Retrieve a workout session by ID
PUT /workout-sessions/<id>: Update an existing workout session
DELETE /workout-sessions/<id>: Delete a workout session
Models
The application uses two models: Member and WorkoutSession. These models are defined in the models.py file.

Routes
The application uses Flask routes to handle API requests. These routes are defined in the routes.py file.

Database
The application uses a SQLite database to store data. The database schema is defined in the models.py file.

Contributing
Contributions are welcome! Please submit a pull request with your changes.

Acknowledgments
This project was created as an assignment for [Assignment Name].
