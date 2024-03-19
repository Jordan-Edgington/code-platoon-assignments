# your improved User class goes here
class User:
    def __init__(self, name, email_address, dln, posts=[]):
        self.name = name
        self.email = email_address
        self.dln = dln
        self.posts = posts

    def __str__(self):
        return f"{self.name}'s email address is {self.email} and their driver's license number is {self.dln}"

    def send_message(self, user):
        return f"Sending a message to {user.name} at {user.email}"

    def create_post(self, message):
        print(message)
        self.posts.append(message)

    def view_posts(self):
        for post in range(0, len(self.posts)):
            print(self.posts[post])

    def del_post(self, post_index):
        self.posts.remove(jordan.posts[post_index])


jordan = User("Jordan", "jordan.edgington.dev@gmail.com", "123456789")
emma = User("Emma", "emma@emmataylor.net", "987654321")

jordan.create_post("This is my first post on the new app!")
jordan.create_post("Post number 2 going up!")
jordan.view_posts()
jordan.del_post(1)
jordan.view_posts()
