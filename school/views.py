from django.shortcuts import render
from .models import Student


def students_list(request):
    template = 'school/students_list.html'
    
    # Оптимизированный запрос с prefetch_related
    students = Student.objects.all().order_by('group').prefetch_related('teachers')
    
    context = {
        'object_list': students,
    }

    return render(request, template, context)