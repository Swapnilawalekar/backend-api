# Backend API – Flask + MySQL

This project is a generic, secure backend REST API built using Flask and MySQL.  
It supports dynamic CRUD operations (Insert, Fetch, Update, Delete) on allowed database tables.

The backend is frontend-agnostic and can be consumed by any client that can send HTTP requests.

---

## Project Structure

backend-api/
│── app.py
│── db_config.py
│── db_connection.py
│── validators.py
│── insert_data.py
│── fetch_data.py
│── update_data.py
│── delete_data.py
│── README.md

---

## Technologies Used

- Python 3
- Flask
- MySQL
- mysql-connector-python
- Git & GitHub

---

## How to Run the Project Locally

### Install dependencies
pip install flask flask-cors mysql-connector-python

### Update database configuration
Edit `db_config.py`:

DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "your_password",
    "database": "emp"
}

### Start the server
python app.py

Server runs at:
http://127.0.0.1:5000

---

## Security Design

- Database credentials are never exposed to frontend
- Only whitelisted tables are accessible
- Parameterized queries prevent SQL injection
- Backend controls schema access

---

## API Endpoints

### Insert Data
POST /insert

Request Body:
{
  "table": "empl2",
  "data": {
    "Eid": 1,
    "Name": "XYZ",
    "Salary": 20000
  }
}

Response:
{
  "message": "Data inserted successfully"
}

---

### Fetch Data
GET /fetch/empl2

Response:
[
  {
    "Eid": 1,
    "Name": "XYZ",
    "Salary": 20000
  }
]

---

### Update Data
PUT /update

Request Body:
{
  "table": "empl2",
  "data": {
    "Salary": 30000
  },
  "condition": {
    "Eid": 1
  }
}

Response:
{
  "message": "Data updated successfully"
}

---

### Delete Data
DELETE /delete

Request Body:
{
  "table": "empl2",
  "condition": {
    "Eid": 1
  }
}

Response:
{
  "message": "Data deleted successfully"
}

---

## Allowed Tables

Allowed tables are defined in `db_config.py`:

ALLOWED_TABLES = ["empl2", "student"]

---

## Testing

- Postman / Thunder Client
- Browser (GET requests)
- Any frontend application

---

## Deployment

This backend can be deployed on Render, Railway, AWS, or Docker-based platforms.  
Frontend developers only need the deployed API URL and this documentation.

---

## Interview Summary

Designed a modular Flask backend with secure MySQL integration, dynamic CRUD APIs, and deployment-ready architecture.

---

## Author

Swapnil Awalekar  
Backend Developer | Python | Flask | MySQL
