from django.db import models
from django.urls import reverse
from .coherte import Cohorte

class Student(models.Model):
    name = models.CharField(max_length=50)
    document_type = models.CharField(max_length=30)
    document_number = models.IntegerField(default=0)
    cohorte = models.ForeignKey(Cohorte, null=True, on_delete=models.SET_NULL)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("student-detail", args=[str(self.id)])
    