# Inheritance - allows a class to inherit attributes and methods from another class
# class that inherits is called a derived or child class
# class that is inherited from is called a base or parent class

# allows code reusability - reuse of the parent code
# hierarchy of classes - parent class can have multiple child classes
# extensibility - can extend the functionality of the parent class by adding new methods ormainta
#  overriding existing ones in the child class
# maintainability - changes made to the parent class are automatically reflected in the child classes

# Base class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Animal speaks"


# Derived class
class Dog(Animal):
    def speak(self):
        return "Woof!"
# Derived class


class Cat(Animal):
    def speak(self):
        return "Meow!"


# Create instances of the derived classes
dog = Dog("Buddy")
cat = Cat("Whiskers")
print(f"{dog.name} says: {dog.speak()}")
print(f"{cat.name} says: {cat.speak()}")

# Types of inheritance
# Single - derived class has only one base class
# Multiple - derived class has more than one base class


class Father:
    def __init__(self):
        self.father_name = "Harry"

    def show_father(self):
        print(f"Father's Name: {self.father_name}")


class Mother:
    def __init__(self):
        self.mother_name = "Sally"

    def show_mother(self):
        print(f"Mother's Name: {self.mother_name}")


class Child(Father, Mother):
    def __init__(self):
        Father.__init__(self)
        Mother.__init__(self)
        self.child_name = "Tommy"

    def show_parents(self):
        self.show_father()
        self.show_mother()
        print(f"Child's Name: {self.child_name}")


child = Child()
child.show_parents()

# Multilevel - a derived class is derived from another derived class


class GrandParent:
    def __init__(self, name):
        self.grandparent_name = name

    def show_grandparent(self):
        print(f"Grandparent's Name: {self.grandparent_name}")


class Parent(GrandParent):
    def __init__(self, gp_name, p_name):
        super().__init__(gp_name)
        self.parent_name = p_name

    def show_parent(self):
        print(f"Parent's Name: {self.parent_name}")


class Child(Parent):
    def __init__(self, gp_name, p_name, c_name):
        super().__init__(gp_name, p_name)
        self.child_name = c_name

    def show_child(self):
        print(f"Child's Name: {self.child_name}")


child2 = Child("Robert", "David", "Manny")
child2.show_grandparent()
child2.show_child()
child2.show_parent()

# Hierarchical - multiple derived classes inherit from a single base class


class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def show_info(self):
        print(f"Make: {self.make}, Model: {self.model}")


class Car(Vehicle):
    def __init__(self, make, model, doors):
        super().__init__(make, model)
        self.doors = doors

    def show_car_info(self):
        self.show_info()
        print(f"Doors: {self.doors}")


class Motorcycle(Vehicle):
    def __init__(self, make, model, type):
        super().__init__(make, model)
        self.type = type

    def show_motorcycle_info(self):
        self.show_info()
        print(f"Type: {self.type}")


class Truck(Vehicle):
    def __init__(self, make, model, capacity):
        super().__init__(make, model)
        self.capacity = capacity

    def show_truck_info(self):
        self.show_info()
        print(f"Capacity: {self.capacity}")


car = Car("Toyota", "Camry", 4)
motorcycle = Motorcycle("Harley-Davidson", "Street 750", "Cruiser")
truck = Truck("Ford", "F-150", "1 Ton")

car.show_car_info()
motorcycle.show_motorcycle_info()
truck.show_truck_info()

# Hybrid - a combination of multiple and multilevel inheritance


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Employee(Person):
    def __init__(self, name, age, employee_id):
        super().__init__(name, age)
        self.employee_id = employee_id


class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id


class TeachingAssistant(Employee):
    def __init__(self, name, age, employee_id):
        Employee.__init__(self, name, age, employee_id)


class ThirdYearStudent(Student):
    def __init__(self, name, age, student_id, year):
        super().__init__(name, age, student_id)
        self.year = year


ta = TeachingAssistant("Alice", 25, "E123")
print(f"Name: {ta.name}, Age: {ta.age}, Employee ID: {ta.employee_id}")
third_year_student = ThirdYearStudent("Bob", 22, "S789", 3)
print(f"Name: {third_year_student.name}, Age: {third_year_student.age}, Student ID: {third_year_student.student_id}, Year: {third_year_student.year}")


# Method Overiding - allows a derived class to provide a specific implementation of a method that is already defined in its base class
# enables a derived class to modify the behavior of a method inherited from the base class without changing the base class's code
# runtime polymorphism - same method call behaves differently based on instance actual class
class Animal:
    def speak(self):
        return "Animal speaks"


class Dog(Animal):
    def speak(self):  # override
        return "Dog barks"


class Cat(Animal):
    def speak(self):  # override
        return "Cat meows"


# Creating instances of the classes
animal = Animal()
dog = Dog()
cat = Cat()
# polymorphic behavior - same method call behaves differently based on instance actual class
print(animal.speak())  # Output: Animal speaks
print(dog.speak())     # Output: Dog barks
print(cat.speak())     # Output: Cat meows

# super() - used to call a method from the parent class in a child class
# allows you to access the parent class's methods and properties without explicitly naming the parent class


class Parent:
    def __init__(self, name):
        self.name = name

    def show_name(self):
        print(f"Parent's Name: {self.name}")


class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)  # call the parent class's __init__ method
        self.age = age

    def show_info(self):
        super().show_name()  # call the parent class's show_name method
        print(f"Child's Age: {self.age}")


child = Child("Alice", 10)
child.show_info()

# isinstance() - checks if an object is an instance of a specific class or a subclass thereof
print(isinstance(child, Child))  # True
print(isinstance(child, Parent))  # True
print(isinstance(child, object))  # True
# issubclass() - checks if a class is a subclass of another class
print(issubclass(Child, Parent))  # True
print(issubclass(Child, object))  # True
print(issubclass(Parent, Child))  # False
