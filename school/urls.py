from django.urls import path
from .views import StudentList  # импортируем класс

urlpatterns = [
    path('students/', StudentList.as_view(), name='students_list'),
]