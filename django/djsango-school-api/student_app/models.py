from django.db import models
from django.core import validators as v
from .validators import validate_name_format
from .validators import validate_combination_format
from .validators import validate_school_email
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

    def __str__(self):
        return f'{self.name} - {self.student_email} - {self.locker_number}'

    def newLockerNumber(self, num):
        self.locker_number = num
        self.save()

    def changeStatus(self, bool):
        self.good_student = bool
        self.save()
