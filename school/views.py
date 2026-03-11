from django.views.generic import ListView
from .models import Student


class StudentList(ListView):
    model = Student
    template_name = 'school/students_list.html'
    ordering = 'group'
    
    def get_queryset(self):
        # Переопределяем метод для оптимизации запросов
        return Student.objects.all().order_by(self.ordering).prefetch_related('teachers')


