from os import system
# when clear() is called, it just clears the terminal to keep things clean
def clear(): return system('clear')

# created class CarManager


class CarManager:
    all_cars = []
    total_cars = 0
    current_selection = None

    # the constructor for the class
    def __init__(self, make, model, year, mileage, services=[]):
        self.make = make
        self.model = model
        self.year = year
        self.mileage = mileage
        self.services = services
        self.id = CarManager.total_cars + 1
        CarManager.total_cars += 1
        CarManager.all_cars.append(self)

    # creating the string that will be printed when print(self) occurs
    def __str__(self):
        return (f"Car: {self.id} | {self.year} {self.make.capitalize()} {self.model.capitalize() } | It has {self.mileage} miles and the following services: {', '.join(self.services).title()}.")

    # this is tells python how to represent each object when represented in my all_cars list
    def __repr__(self):
        return str(self)

    # -----------------------------------------
    #   These are all my getters and setters.
    #   Each requires a str, int, or list
    # -----------------------------------------

    @property
    def make(self):
        return self._make

    @make.setter
    def make(self, new_make):
        if isinstance(new_make, str):
            self._make = new_make
        else:
            print("The Make must be a string.")

    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, new_model):
        if isinstance(new_model, str):
            self._model = new_model
        else:
            print("The Model must be a string.")

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, new_year):
        if isinstance(new_year, int):
            self._year = new_year
        else:
            print("The Year must be an integer.")

    @property
    def mileage(self):
        return self._mileage

    @mileage.setter
    def mileage(self, new_mileage):
        if isinstance(new_mileage, int):
            self._mileage = new_mileage
        else:
            print("The milage must be an integer.")

    @property
    def services(self):
        return self._services

    @services.setter
    def services(self, new_services):
        if isinstance(new_services, list):
            self._services = new_services
        else:
            print("The services must be a list.")

    # -------------------------------------------------------
    #   These are my static methods for the class CarManager
    # -------------------------------------------------------

    # Prompts you for all the info of your new car, then creates the object as new_car
    @staticmethod
    def add_car():
        clear()
        print("Input your new car's information below: ")
        make = input("Enter the Make >> ").capitalize()
        model = input("Enter the model  >> ").capitalize()
        year = int(input("Enter the year  >> "))
        mileage = int(input("Enter the mileage >> "))
        print("Now that you have created your car, you'll have to go add the services.")
        new_car = CarManager(make, model, year, mileage)

    # loops through the all_cars list printing the ID, year, make, and model in a specific format
    @staticmethod
    def view_cars():
        clear()
        for car in CarManager.all_cars:
            print(
                f"Car {car.id}: {car.year} {car.make.capitalize()} {car.model.capitalize()}")
            pass

    # prints CarManager.total_cars

    @staticmethod
    def view_total_cars():
        clear()
        print(f"There are {CarManager.total_cars} cars.")
        pass

    # prints available cars, then prompts user to select one

    @staticmethod
    def select_car():
        clear()
        print("Which car would you like to select from the list below?")
        for car in CarManager.all_cars:
            print(
                f"Car {car.id}: {car.year} {car.make.capitalize()} {car.model.capitalize()}")
        user_input = int(input("Enter a car number from the above list. "))
        clear()
        # if the selected car is a valid input based on the list of cars, set CarManager.current_selection
        if user_input in range(1, CarManager.total_cars + 1):
            CarManager.current_selection = CarManager.all_cars[user_input - 1]
            print(
                f"You have selected car {user_input}, the {CarManager.current_selection.make.capitalize()} {CarManager.current_selection.model.capitalize()}.")
        else:
            CarManager.select_car()

    # ------------------------------------
    #   these are my instance methods
    # ------------------------------------

    # Prints the current car's details
    def view_car_details(self):
        clear()
        print(self)

    # prints the current car, prompts the user to input a service, and updates current_car's services list if valid
    def service_car(self):
        clear()
        print(
            f"Current Car: {self.year} {self.make} {self.model}.\n")
        user_input_two = input(
            "Please enter the service you would like performed >> ")
        if isinstance(user_input_two, str):
            self.services.append(user_input_two)
            print(self.services)
        else:
            print("The service must be a string.")
    # prints the current car, prompts the user to input new mileage, and updates current_car's mileage if valid

    def update_mileage(self):
        clear()
        print(
            f"Current Car: {self.year} {self.make} {self.model}.")
        user_input_two = int(input("Please enter the new mileage >> "))
        if isinstance(user_input_two, int):
            self.mileage = user_input_two
            print(f"New mileage is {self.mileage}.")
        else:
            print("The mileage must be an integer.")


# Created a couple objects of the class "CarManager"
honda = CarManager("honda", "civic", 2022, 45000, ["oil change"])
ford = CarManager("ford", "mustang", 2024, 6,
                  ["oil change", "tires rotated"])


# --------------------------------------------------------------------------------------
# this loop is the running app, printing menus and calling the above static methods
# --------------------------------------------------------------------------------------
run_app = True
while run_app:
    # Prints menu
    if CarManager.current_selection == None:
        print(
            f"Welcome to your terminal Car Manager.\n\n----  TermGarage  ----\n1. Add a car\n2. View all cars\n3. View total number of cars\n4. Select your car\n8. Quit\n\nInput a number correlating to the action you wish to accomplish.")
    else:
        print(
            f"Welcome to your terminal Car Manager.\n\n----  TermGarage  ----\n1. Add a car\n2. View all cars\n3. View total number of cars\n4. Select your car\n5. See your car\'s details\n6. Service your car\n7. Update mileage\n8. Quit\n\nCurrent Car: {CarManager.current_selection.year} {CarManager.current_selection.make.capitalize()} {CarManager.current_selection.model.capitalize()} \n\nInput a number correlating to the action you wish to accomplish.")
    user_input = int(input(">> "))
    match user_input:
        case 1:
            CarManager.add_car()
            clear()
        case 2:
            CarManager.view_cars()
            input("Press enter to continue.")
            clear()
        case 3:
            CarManager.view_total_cars()
            input("Press enter to continue.")
            clear()
        case 4:
            CarManager.select_car()
            input("Press enter to continue")
            clear()
        case 5:
            if CarManager.current_selection == None:
                clear()
                print("You must first select a car.")
                input("Press enter to continue.")
                clear()
            else:
                CarManager.view_car_details(CarManager.current_selection)
                input("Press enter to continue.")
                clear()
        case 6:
            if CarManager.current_selection == None:
                clear()
                print("You must first select a car.")
                input("Press enter to continue.")
            else:
                CarManager.service_car(CarManager.current_selection)
                input("Press enter to continue.")
                clear()
        case 7:
            if CarManager.current_selection == None:
                clear()
                print("You must first select a car.")
                input("Press enter to continue.")
                clear()
            else:
                CarManager.update_mileage(CarManager.current_selection)
                input("Press enter to continue.")
                clear()
        case 8:
            run_app = False
            print("Goodbye! Come back soon!")
