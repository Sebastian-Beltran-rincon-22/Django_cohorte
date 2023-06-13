from django.urls import path

from .views import views
from .views import students

urlpatterns = [
    path ('',views.index,name= "index")
]

urlpatterns += [
    path("students", students.StudentListView.as_view(),name="students"),
    path("students/<int:pk>",students.StudentDetailView.as_view(),name='student-detail'),
    path("students/create", students.StudentCreateView.as_view(),name='create-person')
]