from datetime import date
class Customer:
    def __init__(self, name, bday: date, balance):
        self.name = str(name)
        self.bday = bday
        self.balance = float(balance)


    @property
    def age(self) -> int:
        today = date.today()
        age = today.year - self.bday.year - \
              ((today.month, today.day) < (self.bday.month, self.bday.day))
                # es mtliani guglidan gadmovagde idk
        return age


    def deposit(self, amount):
        if float(amount) > 0:
            self.balance += amount
        else:
            raise ValueError("valshi xar dzmao")


    def withdraw(self, amount):
        if 0 < float(amount) <= self.balance:
            self.balance -= amount
        else:
            raise ValueError("sadgak magdeni puli")


class Bank:
    def __init__(self, name, customers):
        self.name = str(name)
        self.customers = list(customers)


    @property
    def budget(self) -> float:
        return sum(customer.balance for customer in self.customers)


    def add_customer(self, customer):
        self.customers.append(customer)


    def remove_customer(self, customer):
        self.customers.remove(customer)


    def can_get_loan(self, customer, amount):
        if customer.balance >= 0.5 * float(amount):
            return True
        return False

