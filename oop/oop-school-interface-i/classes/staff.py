from classes.person import Person


class Staff(Person):
    def __init__(self, name, age, role, employee_id, password):
        super().__init__(name, age, role)
        self.employee_id = int(employee_id)
        self.password = password

    def __repr__(self):
        return f"{super().__repr__()} | Employee ID: {self.employee_id} | Password: {self.password}"
