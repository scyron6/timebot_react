from timesheets.models import Timesheet, Work
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from .serializers import TimesheetSerializer, WorkSerializer, DetailedTimesheetSerializer

# Timesheet Viewset
class TimesheetViewset(viewsets.ModelViewSet):
    def list(self, request):
        queryset = Timesheet.objects.all()
        permission_classes = [
            permissions.AllowAny
        ]
        serializer = TimesheetSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        queryset = Timesheet.objects.all()
        permission_classes = [
            permissions.AllowAny
        ]
        serializer = DetailedTimesheetSerializer(queryset, many=True)
        return Response(serializer.data)

# Work Viewset
class WorkViewset(viewsets.ModelViewSet):
    queryset = Work.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = WorkSerializer