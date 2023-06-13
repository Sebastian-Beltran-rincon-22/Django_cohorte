from django.shortcuts import render

# Create your views here.
from ..models.students import Student
from ..models.coherte import Cohorte

def index(request):
    """Funtion to home site"""
    cohortes = Cohorte.objects.all()
    students = Student.objects.all()
    
    return render(
        request,
        'attendance/index.html',
        context=
        {
            "cohortes":cohortes,
            "students":students
            
        }
    )
