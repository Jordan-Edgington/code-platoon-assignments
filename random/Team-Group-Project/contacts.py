# create a dictionary that would hold all contacts
contacts_dict = {"Bob Bobbington": "142-145-3653"}

# create a function that lets you create a new contact - edge
# call function with first and last name, then combine them into a full name


def create_contact(first_name, last_name, phone_number):
    full_name = first_name + " " + last_name
    contacts_dict.update({full_name: phone_number})
    return f"Created contact for {contacts_dict[full_name]}"

# create a function that lets you update a contact
# call function with full_name, and then input new first and last names


def update_contact(full_name):
    if full_name in contacts_dict:
        first_name = input("please enter your first Name")
        last_name = input("please enter your last name")
        # if statement if firstname.isalpha() and if lastname.isalpha():
        if first_name.isalpha() == True and last_name.isalpha() == True:
            update_phone = input("please enter your Phone Number")
            update_name = first_name + " " + last_name
            contacts_dict.update({update_name: update_phone})
            del contacts_dict[full_name]
        else:
            print('The input needs to be letters')
    else:
        return f'{full_name} Not found'

# create a function that lets you delete a contact
# Athena's fuctions

# search through dict with full name
# set the loop to find the value
# if the value is in the dictionary remove the item from dictionar
# if not through anwarning message "Contact Not Found"


def delete_contact(full_name):
    if full_name in contacts_dict:
        del contacts_dict[full_name]
        return f"My updated contact list{contacts_dict}"
    else:
        return "Contact not found"


# create a function to view contacts
def view_contacts():
    return print(contacts_dict)


view_contacts()
create_contact("Tony", "Stark", "123-456-7853")
create_contact("Lightning", "McQueen", "123-456-7890")
update_contact("Lightning McQueen")
delete_contact("Bob Bobbington")
view_contacts()
