from django.db import models

from .students import Student


class Attendance(models.Model):
    status = models.BooleanField(default=False)
    excusse = models.BooleanField(default=False)
    excusse_support = models.CharField(max_length=50)
    date = models.DateField(auto_now=True)
    student = models.ForeignKey(Student,on_delete=models.CASCADE)