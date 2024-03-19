# your User class goes here
class User:
    def __init__(self, name, email_address, dln):
        self.name = name
        self.email = email_address
        self.dln = dln

    def __str__(self):
        return f"{self.name}'s email address is {self.email} and their driver's license number is {self.dln}"

    def send_message(self, user):
        return f"Sending a message to {user.name} at {user.email}"


jordan = User("Jordan", "jordan.edgington.dev@gmail.com", "123456789")
emma = User("Emma", "emma@emmataylor.net", "987654321")

print(jordan)
print(emma)
print(jordan.send_message(emma))
