from django.db import models
from django.core import validators as v
from .validators import validate_subject_format, validate_professor_name
from student_app.models import Student
# Create your models here.


class Subject(models.Model):
    subject_name = models.CharField(unique=True, validators=[
                                    validate_subject_format])
    professor = models.CharField(unique=False, validators=[
                                 validate_professor_name])
    students = models.ManyToManyField(
        Student, related_name='subjects', unique=False)

    def __str__(self):
        return f'{self.subject_name} - {self.professor} - {self.students.count()}'

    def add_a_student(self, id):
        if self.students.count() < 31:
            self.students.add(id)
        else:
            raise Exception('This subject is full!')

    def drop_a_student(self, id):
        if id in self.students.all():
            self.students.remove(id)
        else:
            raise Exception('This subject is empty!')
