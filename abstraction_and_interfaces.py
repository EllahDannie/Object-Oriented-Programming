# abstraction
# 1 abstract class usedwithin same class
# interface- can be implemented several times in different classes
# abstraction involves showing only the essential featuresof an obect an hiding the internal details

#
from abc import ABC, abstractmethod

import car


class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount):
        pass


class CreditCardPayment(PaymentMethod):
    def pay(self, amount):
        return f"Paid KES {amount} using Credit Card"


class DebitCardPayment(PaymentMethod):
    def pay(self, amount):
        return f"Paid KES {amount} using Debit Card"


class PayPalPayment(PaymentMethod):
    def pay(self, amount):
        return f"Paid KES {amount} using PayPal"


def process_payment(payment_method: PaymentMethod, amount):
    print(payment_method.pay(amount))


credit_card_payment = CreditCardPayment()
debit_card_payment = DebitCardPayment()
paypal_payment = PayPalPayment()

process_payment(credit_card_payment, 600)
process_payment(debit_card_payment, 100)
process_payment(paypal_payment, 300)


# overriding - when a child class has a method with the same name as a method in the parent class, the child class method overrides the parent class method
# overloading - when a class has multiple methods with the same name but different parameters, the method that is called is determined by the number and type of arguments passed to the method

class Vehicle(ABC):
    @abstractmethod
    def move(self):
        pass


class Car(Vehicle):
    def move(self):
        return "Car is moving on the road"


class Bus(Vehicle):
    def move(self):
        return "Bus is moving on the road"


class Train(Vehicle):
    def move(self):
        return "Train is moving on the road"


def move_vehicle(vehicle: Vehicle):
    print(vehicle.move())


car = Car()
bus = Bus()
train = Train()

vehicles = [Car(), Bus(), Train()]

for v in vehicles:
    move_vehicle(v)


class Notification(ABC):
    @abstractmethod
    def send():
        pass


class EmailNotification(Notification):
    def send(self):
        return "Sending email notification"


class SMSNotification(Notification):
    def send(self):
        return "Sending email notification"


class EmailNotification(Notification):
    def send(self):
        return "Sending email notification"


def send(notification: Notification):
    print(notification.send())


email = EmailNotification()
sms = SMSNotification()


notifications = [EmailNotification(), SMSNotification()]
for n in notifications:
    send(n)
#  abstraction - creating a rule that all classes must follow, without saying how they should do it
# what makes a class abstract is the presence of at least one abstract method, which is a method that is declared but not implemented in the abstract class. The abstract method must be implemented by any concrete subclass that inherits from the abstract class.
# the class cannot be instantiated directly, and it serves as a blueprint for other classes to follow. An abstract class can also contain concrete methods, which are methods that have an implementation in the abstract class and can be inherited by the concrete subclasses.
# An interface is a type of abstract class that only contains abstract methods and no concrete methods. An interface defines a contract that any class that implements it must follow, but it does not provide any implementation details. In Python, we can use the abc module to create abstract classes and interfaces.


class PaymentMethod:
    def pay(self, amount):
        pass


class MpesaPayment(PaymentMethod):
    def pay(self, amount):
        return f"Paid {amount} via M-Pesa"


class CardPayment(PaymentMethod):
    def pay(self, amount):
        return f"Paid {amount} via Card"


def process_payment(payment_method, amount):
    print(payment_method.pay(amount))


payments = [MpesaPayment(), CardPayment()]

for p in payments:
    process_payment(p, 500)


# Interfaces
# An interface is a type of abstract class that only contains abstract methods and no concrete methods.
# An interface defines a contract that any class that implements it must follow, but it does not provide any implementation details.
# In Python, we can use the abc module to create abstract classes and interfaces.
