from django.db import models

class Timesheet(models.Model):
    name = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()
    submission_date = models.DateField(auto_now_add=True)

class Work(models.Model):
    timesheet = models.ForeignKey(Timesheet, related_name='works', on_delete=models.CASCADE)
    employee = models.CharField(max_length=100)
    client = models.CharField(max_length=100)
    work = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    task = models.CharField(max_length=100)
    minutes = models.IntegerField()
    date = models.DateField()