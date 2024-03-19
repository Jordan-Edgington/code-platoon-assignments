from classes.student import Student
from classes.staff import Staff
import csv


class School:
    staff_list = []
    students_list = []

    def __init__(self, name):
        self.name = name
        self.staff = School.all_staff()
        self.students = School.all_students()
    pass

    @classmethod
    def all_students(cls):
        with open("./data/students.csv", 'r', newline='') as csvfile:
            student_data_reader = csv.DictReader(csvfile)
            for student_data in student_data_reader:
                a_student = Student(**student_data)
                cls.students_list.append(a_student)
            return cls.students_list

    @classmethod
    def all_staff(cls):
        with open("./data/staff.csv", 'r', newline='') as csvfile:
            staff_data_reader = csv.DictReader(csvfile)
            for staff_data in staff_data_reader:
                a_staff = Staff(**staff_data)
                cls.staff_list.append(a_staff)
            return cls.staff_list

    def find_student_by_id(self, student_id):
        for student in self.students:
            if student.school_id == int(student_id):
                return student
