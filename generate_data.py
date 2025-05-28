# generate_data.py

import os
import django
import random
from datetime import datetime, timedelta

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'employee_project.settings')
django.setup()

from employee_app.models import Employee, PerformanceRecord, Attendance

from faker import Faker

fake = Faker()

# Generate random Employees
def create_employees(n=10):
    for _ in range(n):
        Employee.objects.create(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            email=fake.unique.email(),
            department=random.choice(['IT', 'HR', 'Finance', 'Marketing']),
            hire_date=fake.date_between(start_date='-5y', end_date='today'),
            phone_number=fake.phone_number()[:15],
            address=fake.address(),
            job_title=random.choice(['Developer', 'Manager', 'Analyst', 'Designer']),
            salary=round(random.uniform(30000, 120000), 2),
            date_of_birth=fake.date_of_birth(minimum_age=22, maximum_age=60),
            gender=random.choice(['Male', 'Female', 'Other']),
            emergency_contact=fake.phone_number(),
            marital_status=random.choice(['Single', 'Married', 'Divorced']),
        )

# Generate random Performance Records
def create_performance_records():
    employees = Employee.objects.all()
    for employee in employees:
        for _ in range(random.randint(1, 5)):
            PerformanceRecord.objects.create(
                employee=employee,
                review_date=fake.date_between(start_date='-1y', end_date='today'),
                score=random.randint(1, 5),
                notes=fake.sentence(),
                project_name=fake.bs(),
                reviewer=fake.name(),
                goals=fake.sentence(),
                strengths=fake.sentence(),
                weaknesses=fake.sentence(),
                training_needs=fake.sentence(),
            )

# Generate random Attendance Records
def create_attendance_records():
    employees = Employee.objects.all()
    for employee in employees:
        for _ in range(random.randint(10, 20)):
            status = random.choice(['Present', 'Absent', 'Leave'])
            check_in = fake.time() if status == 'Present' else None
            check_out = fake.time() if status == 'Present' else None
            Attendance.objects.create(
                employee=employee,
                date=fake.date_between(start_date='-30d', end_date='today'),
                status=status,
                check_in_time=check_in,
                check_out_time=check_out,
                remarks=fake.sentence(),
                work_location=random.choice(['Office', 'Home', 'Remote']),
                shift=random.choice(['Morning', 'Evening', 'Night']),
                overtime_hours=round(random.uniform(0, 3), 2) if status == 'Present' else 0,
                late_reason=fake.sentence() if status == 'Present' else '',
            )

if __name__ == "__main__":
    print("Creating Employees...")
    create_employees(10)
    print("Creating Performance Records...")
    create_performance_records()
    print("Creating Attendance Records...")
    create_attendance_records()
    print("Done seeding data!")
