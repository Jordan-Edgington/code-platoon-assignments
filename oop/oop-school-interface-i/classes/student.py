from classes.person import Person


class Student(Person):
    def __init__(self, name, age, role, school_id, password):
        super().__init__(name, age, role)
        self.school_id = int(school_id)
        self.password = password

    def __repr__(self):
        return f"{super().__repr__()} | School ID: {self.school_id} | Password: {self.password}"
