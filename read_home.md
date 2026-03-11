# Проделанная работа:  
**Основное задание:**  
1. Изменена модель с ForeignKey на ManyToManyField
Стало
teachers = models.ManyToManyField(Teacher, related_name='students', verbose_name='Учителя')

2. Создана и применена миграция  
python manage.py makemigrations  
python manage.py migrate

3. Обновлен шаблон html  
  
{% for teacher in student.teachers.all %}  
    <p>{{ teacher.name }} ({{ teacher.subject }})</p>  
{% endfor %}  

4. Загружены данные  

   python manage.py loaddata orm_migrations/school.json

   Получено подтверждение по загрузке:
   Installed 6 object(s) from 1 fixture(s)


   **Дополнительное задание:**
   
Оптимизированы запросы с prefetch_related  (views.py):  
students = Student.objects.all().order_by('group').prefetch_related('teachers')  

   
