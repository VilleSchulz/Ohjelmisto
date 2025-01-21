class Restaurant:
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type
        self.isOpen = False

    def describe_restaurant(self):
        return print(f"{self.name} serves wonderful {self.cuisine_type}.")

    def open_restaurant(self):
        self.isOpen = True
        return print(f"{self.name} is open. Come on in!")


