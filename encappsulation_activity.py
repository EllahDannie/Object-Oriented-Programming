# Exercise Objective
class Employee:
    def __init__(self, name, salary, employee_id):
        self.__name = name
        self.__salary = salary
        self.__employee_id = employee_id

    def get_name(self):
        return self.__name

    def set_salary(self, salary):
        if salary > 0:
            self.__salary = salary
        else:
            raise ValueError("Salary must be positive")

    def get_salary(self):
        return self.__salary

    def get_employee_id(self):
        return self.__employee_id

    def employee_info(self):
        print(
            f"Employee ID: {self.__employee_id}, Name: {self.__name}, Salary: {self.__salary}")


employee = Employee("Lily Kane", 3000, "E123")
print(employee.employee_info())
employee.set_salary(4000)
print(employee.employee_info())

# exercise 2


class Employee:
    def __init__(self, name, salary, employee_id):
        self.__name = name
        self.__salary = salary
        self.__employee_id = employee_id

    @property
    def name(self):
        return self.__name

    @property
    def salary(self):
        return self.__salary

    @property
    def employee_id(self):
        return self.__employee_id

    @salary.setter
    def salary(self, monthly_salary):
        if monthly_salary > 0:
            self.__salary = monthly_salary
        else:
            raise ValueError("Salary must be positive")

    def annual_salary(self):
        return self.__salary * 12

    def employee_info(self):
        return f"Employee ID: {self.__employee_id}, Name: {self.__name}, Salary: {self.__salary}"


employee = Employee("Lily Kane", 3000, "E123")
employee.employee_info
employee.salary = 4000
print(f"Lily Kane's annual salary is: {employee.annual_salary()}")

# exercise 3


class Employee:
    def __init__(self, name, employee_id, salary):
        self._name = name
        self._employee_id = employee_id
        self._salary = salary

    def display_info(self):
        print(
            f"Employee's ID: {self._employee_id}, Name: {self._name}, Salary: {self._salary}")


class Manager(Employee):
    def __init__(self, name, employee_id, salary, bonus_percentage):
        super().__init__(name, employee_id, salary)
        self.__bonus_percentage = bonus_percentage

    @property
    def bonus_percentage(self):
        return self.__bonus_percentage

    def total_compensation(self):
        bonus = self._salary * (self.__bonus_percentage / 100)
        return self._salary + bonus

    def display_info(self):
        super().display_info()
        print(
            f"Bonus Percentage: {self.__bonus_percentage}%, Total Compensation: {self.total_compensation()}")


manager = Manager("Alice Smith", "M456", 5000, 20)
manager.display_info()
