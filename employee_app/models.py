from django.db import models

class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    department = models.CharField(max_length=100)
    hire_date = models.DateField()
    phone_number = models.CharField(max_length=15, blank=True)
    address = models.TextField(blank=True)
    job_title = models.CharField(max_length=100, blank=True)
    salary = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    date_of_birth = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=10, blank=True)
    emergency_contact = models.CharField(max_length=100, blank=True)
    marital_status = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class PerformanceRecord(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='performance_records')
    review_date = models.DateField()
    score = models.IntegerField()
    notes = models.TextField(blank=True)
    project_name = models.CharField(max_length=100, blank=True)
    reviewer = models.CharField(max_length=100, blank=True)
    goals = models.TextField(blank=True)
    strengths = models.TextField(blank=True)
    weaknesses = models.TextField(blank=True)
    training_needs = models.TextField(blank=True)

    def __str__(self):
        return f"{self.employee} - {self.review_date}"

class Attendance(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='attendance_records')
    date = models.DateField()
    status = models.CharField(max_length=20, choices=[('Present', 'Present'), ('Absent', 'Absent'), ('Leave', 'Leave')])
    check_in_time = models.TimeField(null=True, blank=True)
    check_out_time = models.TimeField(null=True, blank=True)
    remarks = models.TextField(blank=True)
    work_location = models.CharField(max_length=100, blank=True)
    shift = models.CharField(max_length=50, blank=True)
    overtime_hours = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    late_reason = models.TextField(blank=True)

    def __str__(self):
        return f"{self.employee} - {self.date} ({self.status})"
