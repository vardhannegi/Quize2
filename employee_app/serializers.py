from rest_framework import serializers
from .models import Employee, PerformanceRecord, Attendance

class PerformanceRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = PerformanceRecord
        fields = '__all__'

class EmployeeSerializer(serializers.ModelSerializer):
    performance_records = PerformanceRecordSerializer(many=True, read_only=True)

    class Meta:
        model = Employee
        fields = '__all__'


class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = '__all__'