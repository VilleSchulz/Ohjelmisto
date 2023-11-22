class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def plot(self):
        print(f"--My name is {self.first_name} {self.last_name}")


class Student(Person):
    def __init__(self, first_name, last_name, id):
        super().__init__(first_name, last_name)
        self.id = id

    def plot(self):
        print(f"--My name is {self.first_name} {self.last_name} and my student number is {self.id}")
        # pääohjelma

p1 = Person("James", "Bond")
s1 = Student("Johnny", "English", 321)
p1.plot()
s1.plot()