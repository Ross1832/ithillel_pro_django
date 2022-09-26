"""
LESSON 12
#in settings.py
if DEBUG = True
    SHELL_PLUS = 'ipython'
    SHELL_PLUS_PRINT_SQL = True
#
Student.object.get_or_create(first_name='Firstname1', last_name='Lastname1')
#
Student.object.update_or_create(first_name='Firstname1', last_name='Lastname1', defaults={"first_name": "FirstName2"})
#
students = Student.objects.all()
students = Student.objects.first()
students = Student.objects.last()
students = Student.objects.get(id=5)
students.first_name = 'FirstName10'
students.save()
students = Student.objects.filter(first_name='Name1')
student = students[1]
student.last_name='LastName10'
students.save()
for s in students:
    s.birthday = '01.01.0001'
    s.save()
students = Student.objects.filter(first_name='Name1').delete()
python manage.py flush
"""