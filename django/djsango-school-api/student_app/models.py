from django.db import models

# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=50, null=False, unique=False)
    student_email = models.EmailField(max_length=100, null=False, unique=True)
    personal_email = models.EmailField(max_length=100, null=True, unique=True)
    locker_number = models.IntegerField(null=False, unique=True, default=110)
    locker_combination = models.CharField(
        max_length=8, null=False, unique=False, default='12-12-12')
    good_student = models.BooleanField(null=False, unique=False, default=True)

    def __str__(self):
        return f'{self.name} - {self.student_email} - {self.locker_number}'

    def newLockerNumber(self, num):
        self.locker_number = num
        self.save()

    def changeStatus(self, bool):
        self.good_student = bool
        self.save()
