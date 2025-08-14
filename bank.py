class Account():
    def __init__(self,id, balance=0):
        self.id = id
        self.balance = balance

    def deposit(self, money):
        if money > 0:
            self.balance += money
            print(f"На счет {self.id} поступило {money} рублей. Теперь на счету {self.balance} рублей.")

    def withdraw(self, money):
        if money > self.balance:
            print(f"На счету {self.id} недостаточно средств для снятия указанной суммы")
        elif money <= self.balance:
            self.balance -= money
            print(f"Со счета {self.id} снято {money} рублей. Теперь на счету {self.balance} рублей.")

    def all_balance(self):
        print(f"На счете {self.id} {self.balance} рублей.")

man = Account("123456789", 600)
man.all_balance()
man.withdraw(450)
man.withdraw(800)
man.deposit(23000)
man.all_balance()

