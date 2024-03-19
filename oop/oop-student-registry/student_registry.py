student_counter = 0


class Student:
    def __init__(self, name, age=13, grade="12th"):
        # turns student counter to a global variable, that will be incremented by 1 for each student initialized
        global student_counter
        student_counter += 1
        self.name = name
        self.age = age
        self.grade = grade
        self.id = student_counter

    def __str__(self):
        return f"Student {self.id}: Name: {self._name}, Age: {self._age}, Grade: {self._grade}"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str) and len(new_name) >= 3 and new_name.isalpha() is True and new_name.istitle() is True:
            self._name = new_name
        else:
            print("Name must be a string that contains 3 or more characters, all letters, and is in the title format.")

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, new_age):
        if isinstance(new_age, int) and 11 < new_age < 18:
            self._age = new_age
        else:
            print("Name must be a integer between 11 and 18.")

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, new_grade):
        if 2 < len(new_grade) <= 4 and new_grade[-2:] == "th" and 9 <= int(new_grade[:-2]) <= 12:
            self._grade = new_grade
        else:
            print("The grade must be between 9th and 12th and must end with th.")


jordan = Student(7)
