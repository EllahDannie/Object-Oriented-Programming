# Design a Class Hierarchy

class Person:  # base class
    def __init__(self, name, id, email):
        self.name = name
        self.id = id
        self.email = email

    def display_info(self):
        print(f"Name: {self.name}, ID: {self.id}, Email: {self.email}")

    def send_email(self, recipient_email, subject, message):
        print(
            f"Sending email to {recipient_email} with subject '{subject}' and message: {message}")


class Student(Person):  # derived class inheriting from Person
    def __init__(self, name, id, email, major, course, gpa):
        super().__init__(name, id, email)
        self.major = major
        self.course = course
        self.gpa = gpa

    def enroll_course(self, course):
        print(f"{self.name} has enrolled in {course}.")
        return course

    def calculate_gpa(self, grades):
        if len(grades) == 0:
            return 0
        self.gpa = sum(grades) / len(grades)
        print(f"{self.name}'s GPA is: {self.gpa}")
        return self.gpa


class Lecturer(Person):
    def __init__(self, name, id, email, department, salary, course_teaching):
        super().__init__(name, id, email)
        self.department = department
        self.course = course_teaching
        self.salary = salary

    def assign_course(self, course):
        print(f"{self.name} has been assigned to teach {course}.")
        return course

    def calculate_salary(self, hours_worked):
        self.salary = hours_worked * 50  # Assuming $50 per hour
        print(f"{self.name}'s salary is: {self.salary}")
        return self.salary


class Staff(Person):
    def __init__(self, name, id, email, position, department, hourly_rate):
        super().__init__(name, id, email)
        self.department = department
        self.position = position
        self.hourly_rate = hourly_rate

    def pay_roll(self, hours_worked):
        salary = hours_worked * self.hourly_rate
        print(f"{self.name}'s payroll is: {salary}")
        return salary


student = Student("Daniellah Jerotich", "S123", "ellahdannie@example.com",
                  "Computer Science", "Data Structures", 3.5)
lecturer = Lecturer("Mr. Luke", "L456", "luke.professor@example.com",
                    "Computer Science", 80000, "Data Structures")
staff = Staff("Bob", "S789", "bob.staff@example.com",
              "Administration", "Office Manager", 25)
student.display_info()  # overriding the display_info method from the Person class
lecturer.display_info()
staff.display_info()
student.enroll_course("Algorithms")
student.calculate_gpa([3.5, 3.7, 3.8])
lecturer.assign_course("Operating Systems")
lecturer.calculate_salary(160)
staff.pay_roll(160)
