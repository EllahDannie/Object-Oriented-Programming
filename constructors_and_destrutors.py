class Student:
    def __init__(self):
        self.name = 'Unknown'
        self.age = 0


class Children:
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email

    def create(self):
        print(f"{self.name} is {self.age} years old.\nEmail address: {self.email}")


child1 = Children("Lara", 23, "lara@gmail.com")
child2 = Children("Megan", 21, "girllee@gmail.com")
child1.create()
child2.create()


class Vegetables:
    def __init__(self, name="Unknown", color="Green", price=0):
        self.name = name
        self.color = color
        self.price = price

    def display(self):
        print(f"Name: {self.name}")
        print(f"Color: {self.color}")
        print(f"Price: {self.price}")


veg1 = Vegetables()

veg2 = Vegetables("Carrot", "Orange", 50)

veg3 = Vegetables("Spinach")


veg1.display()
print()
veg2.display()
print()
veg3.display()


class Fruits:
    def __init__(self, name="Unknown"):
        self.name = name
        print(f"{self.name} was created")

    def __del__(self):
        print(f"{self.name} was destroyed")


fruit1 = Fruits("Apple")
fruit2 = Fruits("Mango")
fruit3 = Fruits("Banana")

del fruit1
