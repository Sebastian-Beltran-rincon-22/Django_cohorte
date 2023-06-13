from django.contrib import admin

# Register your models here.
from .models.coherte import Cohorte
from .models.students import Student
from .models.attendance import Attendance

admin.site.register(Cohorte)
admin.site.register(Student)
admin.site.register(Attendance)

