class Student:
    class_year = 2024
    num_students = 0
    course_name = "Object-Oriented Programming"

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.num_students += 1


student1 = Student("Spongebob", 23)
student2 = Student("Patrick", 26)
student3 = Student("Squidward", 30)

print(student1.name)

print(Student.class_year)
print(Student.course_name)
print(Student.num_students)

print(f"{student1.name}, {student1.age}")


class Animal:
    def __init__(self, name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")


class Dog(Animal):
    pass


class Cat(Animal):
    pass


class Mouse(Animal):
    pass


dog = Dog("Scooby")
cat = Cat("Tom")
mouse = Mouse("Jerry")

print(dog.name)
print(dog.is_alive)

dog.eat()

print(
    f"The owner left for work. {dog.name} is sleeping, while {cat.name} is busy chasing {mouse.name} around the house")


class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")


class Prey(Animal):
    def flee(self):
        print(f"{self.name} is fleeing")


class Predator(Animal):
    def hunt(self):
        print(f"{self.name} is hunting")


class Rabbit(Prey):
    pass


class Hawk(Predator):
    pass


class Fish(Prey, Predator):
    pass


rabbit = Rabbit("Bugs")
hawk = Hawk("Sky")
fish = Fish("Nemo")

fish.eat()
fish.sleep()


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
