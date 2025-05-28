from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.throttling import UserRateThrottle
from .models import Employee, PerformanceRecord, Attendance
from .serializers import EmployeeSerializer, PerformanceRecordSerializer, AttendanceSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def employee_summary(request):
    data = Employee.objects.values('department').annotate(count=models.Count('id'))
    return Response(data)


class EmployeeThrottle(UserRateThrottle):
    rate = '10/min'

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['first_name', 'last_name', 'department']
    ordering_fields = ['hire_date', 'department']
    throttle_classes = [EmployeeThrottle]
    # permission_classes = [IsAuthenticated]

class PerformanceRecordViewSet(viewsets.ModelViewSet):
    queryset = PerformanceRecord.objects.all()
    serializer_class = PerformanceRecordSerializer
    # permission_classes = [IsAuthenticated]


class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
    # permission_classes = [IsAuthenticated]
