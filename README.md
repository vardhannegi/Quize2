
# Project Setup and API Documentation

This project is managed with **[uv](https://github.com/astral-sh/uv)**, a fast Python package manager. 

### 📦 Package Manager Setup

If you don’t have `uv` installed, you can set it up using:
```bash
pip install uv
```

Then, install all dependencies with:
```bash
uv sync
```

---

### 🚀 How to Run the Project
1. Run database container:
   ```bash
   docker run --name=empdb -p 5432:5432 -e POSTGRES_DB=empdb -e POSTGRES_USER=root -e POSTGRES_PASSWORD=pass -d postgres
   ```

2. Apply database migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

3. Create a superuser:
   ```bash
   python manage.py createsuperuser
   ```

4. Apply authentication token migrations:
   ```bash
   python manage.py migrate authtoken
   ```

5. Generate an authentication token for your superuser:
   ```bash
   python manage.py drf_create_token <your_superuser_username>
   ```

6. Generate fake data:
   ```bash
   python generate_data.py
   ```

7. Start the server:
   ```bash
   python manage.py runserver 8000
   ```

---

### 📚 API Endpoints

| Endpoint                         | Method | Example URL                                        | Example Body / Description                                                        |
| -------------------------------- | ------ | -------------------------------------------------- | --------------------------------------------------------------------------------- |
| `/api/employees/`                | POST   | `http://127.0.0.1:8000/api/employees/`             | Create a new employee. See [Employee POST Body](#employee-post-body).             |
| `/api/employees/{id}/`           | PUT    | `http://127.0.0.1:8000/api/employees/1/`           | Update an employee. See [Employee PUT Body](#employee-put-body).                  |
| `/api/employees/{id}/`           | DELETE | `http://127.0.0.1:8000/api/employees/1/`           | Delete an employee.                                                               |
| `/api/performance-records/`      | POST   | `http://127.0.0.1:8000/api/performance-records/`   | Create a performance record. See [Performance POST Body](#performance-post-body). |
| `/api/performance-records/{id}/` | PUT    | `http://127.0.0.1:8000/api/performance-records/1/` | Update a performance record. See [Performance PUT Body](#performance-put-body).   |
| `/api/performance-records/{id}/` | DELETE | `http://127.0.0.1:8000/api/performance-records/1/` | Delete a performance record.                                                      |
| `/api/attendance/`               | POST   | `http://127.0.0.1:8000/api/attendance/`            | Create an attendance record. See [Attendance POST Body](#attendance-post-body).   |
| `/api/attendance/{id}/`          | PUT    | `http://127.0.0.1:8000/api/attendance/1/`          | Update an attendance record. See [Attendance PUT Body](#attendance-put-body).     |
| `/api/swagger/`                  | GET    | `http://127.0.0.1:8000/api/swagger/`               | Swagger API documentation.                                                        |
| `/api-token-auth/`               | POST   | `http://127.0.0.1:8000/api-token-auth/`            | Obtain authentication token.                                                      |
---

### 🔧 Example API Payloads

#### Create an Employee (`POST /api/employees/`)
```json
{
  "first_name": "John",
  "last_name": "Doe",
  "email": "john.doe@example.com",
  "department": "IT",
  "hire_date": "2023-05-20",
  "phone_number": "1234567890",
  "address": "123 Main Street, City, Country",
  "job_title": "Software Engineer",
  "salary": 75000.00,
  "date_of_birth": "1990-01-01",
  "gender": "Male",
  "emergency_contact": "0987654321",
  "marital_status": "Single"
}
```

#### Create a Performance Record (`POST /api/performance-records/`)
```json
{
  "employee": 1,
  "date": "2024-10-10",
  "rating": 4,
  "feedback": "Excellent work on the recent project.",
  "project_name": "Website Redesign",
  "reviewer": "Jane Smith",
  "goals": "Improve front-end performance.",
  "strengths": "Good problem-solving skills.",
  "weaknesses": "Needs to work on time management.",
  "training_needs": "Advanced JavaScript training."
}
```

#### Create an Attendance Record (`POST /api/attendance/`)
```json
{
  "employee": 1,
  "date": "2024-10-15",
  "status": "Present",
  "check_in_time": "09:00:00",
  "check_out_time": "17:30:00",
  "remarks": "Worked from home.",
  "work_location": "Home",
  "shift": "Morning",
  "overtime_hours": 1.5,
  "late_reason": "Traffic jam in the morning."
}
```

#### Get an Token (`POST /api-token-auth/`)
```json
{
    "username": "<your_username>",
    "password": "<your_password>"
}
```

---
