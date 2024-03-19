class ContactList:

    def __init__(self, name, contact_list):
        self._name = name
        self._contacts = contact_list

    @property
    def get_contacts(self):
        return self._contacts

    @get_contacts.setter
    def set_contacts(self, contact_list):
        if isinstance(contact_list, list):
            self._contacts = contact_list

    @property
    def get_name(self):
        return self._name

    @get_name.setter
    def set_name(self, name):
        if isinstance(name, str):
            self._name = name

    def add_contact(self, contact):
        self._contacts.append(contact)

    def remove_contact(self, contact_name):
        for friend in self._contacts:
            if contact_name == friend["name"]:
                self._contacts.remove(friend)

    def find_shared_contacts(self, list_name):
        shared_list = []
        for friend in self._contacts:
            if friend in list_name._contacts:
                shared_list.append(friend)
        return shared_list


friends = [{'name': 'Alice', 'number': '867-5309'},
           {'name': 'Bob', 'number': '555-5555'}]
work_buddies = [{'name': 'Alice', 'number': '867-5309'},
                {'name': 'Carlos', 'number': '555-5555'}]

my_friends_list = ContactList('My Friends', friends)
my_work_buddies = ContactList('Work Buddies', work_buddies)

friends_i_work_with = my_friends_list.find_shared_contacts(my_work_buddies)
print(f"You work with the following friend: {friends_i_work_with}.")
print(my_friends_list._contacts)
my_friends_list.remove_contact('Alice')
print(my_friends_list._contacts)
# friends_i_work_with should be: [{'name':'Alice','number':'867-5309'}]
