from rest_framework import serializers
from timesheets.models import Timesheet, Work

# Work Serializer
class WorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Work
        fields = '__all__'

# Timesheet Serializer
class TimesheetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Timesheet
        fields = '__all__'

class DetailedTimesheetSerializer(serializers.ModelSerializer):
    works = WorkSerializer(many=True)
    class Meta:
        model = Timesheet
        fields = '__all__'