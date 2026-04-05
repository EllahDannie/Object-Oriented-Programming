class Bank_Account:
    def __init__(self, account_number, account_holder, initial_balance):
        self._account_number = account_number
        self.account_holder = account_holder
        self.balance = 0

        if initial_balance >= 0:
            self.balance = initial_balance
        else:
            print("Initial balance cannot be negative.")

    @property
    def account_number(self):
        return self._account_number

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, amount):
        if amount >= 0:
            self._balance = amount
        else:
            print("Balance cannot be negative.")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(
                f"You have successfully deposited {amount}. Your new balance is: {self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("You have insufficient funds in your account.")
        else:
            self.balance -= amount
            print(
                f"You have successfully withdrawn {amount}. New balance: {self.balance}")

    def get_balance(self):
        return self.balance

    def display_account_info(self):
        print(f"Account Number: {self.account_number}")
        print(f"Account Holder: {self.account_holder}")
        print(f"Balance: {self.balance}")


account1 = Bank_Account(345213, "John Nolan", 1000)
account1.display_account_info()

account1.deposit(500)
account1.withdraw(20000)
account1.withdraw(300)

print(f"Your current Balance is: {account1.get_balance()}")
