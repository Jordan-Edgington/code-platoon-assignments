from django.db import models
from django.core import validators as v
from .validators import validate_name_format
from .validators import validate_combination_format
from .validators import validate_school_email
from subject_app.models import Subject
# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=50, null=False,
                            unique=False, validators=[validate_name_format])  # Regex Validator
    student_email = models.EmailField(
        max_length=100, null=False, unique=True, validators=[validate_school_email])  # Regex validator
    personal_email = models.EmailField(
        max_length=100, null=True, unique=True)  # No validator
    locker_number = models.IntegerField(null=False, unique=True, default=110, validators=[
                                        v.MaxValueValidator(200), v.MinValueValidator(1)])  # MinVal/MaxVal validators
    locker_combination = models.CharField(
        null=False, unique=False, default='12-12-12', validators=[v.MaxLengthValidator(8), validate_combination_format])  # Regex validator
    good_student = models.BooleanField(
        null=False, unique=False, default=True)  # No validator
    subjects = models.ManyToManyField(
        Subject, related_name='students', unique=False)

    def __str__(self):
        return f'{self.name} - {self.student_email} - {self.locker_number}'

    def newLockerNumber(self, num):
        self.locker_number = num
        self.save()

    def changeStatus(self, bool):
        self.good_student = bool
        self.save()

    def add_subject(self, id):
        if self.subjects.count() < 8:
            print(self.subjects.all())
            if self.subjects.filter(id=id):
                raise Exception('This student is already taking that class!')
            else:
                self.subjects.add(id)

        else:
            raise Exception('This students class schedule is full!')

    def remove_subject(self, id):
        if id in self.subjects.all():
            self.subjects.remove(id)
        else:
            raise Exception('This students class schedule is empty!')
