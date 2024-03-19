class Person:
    '''
    Person class. Parent class for students, staff
    '''

    def __init__(self, name, age, role):
        self.name = name
        self.age = int(age)  # TODO: Handle casting error if age invalid
        self.role = role

    def __str__(self):
        return f"{self.name.upper()}\n----------\nAge: {self.age}\nRole: {self.role}."

    def __repr__(self):
        return str(self)
