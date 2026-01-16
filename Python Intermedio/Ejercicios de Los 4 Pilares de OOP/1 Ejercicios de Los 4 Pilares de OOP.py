#Cree una clase de BankAccount que:
#Tenga un atributo de balance.
#Tenga un método para ingresar dinero.
#Tengo un método para retirar dinero.
#Cree otra clase que herede de esta llamada SavingsAccount que:
#Tenga un atributo de min_balance que se pueda asignar al crearla.
#Arroje un error si al intentar retirar dinero, el retiro haría que el balance quede debajo del min_balance. Es decir que sí se pueden hacer retiros siempre y cuando el balance quede arriba del min_balance.

class BankAccount:
    def __init__(self, balance):
        self.balance = balance
    
    def deposit(self, amount):
        self.balance + amount
    
    def withdraw(self, amount):
        if self.balance < amount:
            raise ValueError("Not enough balance")
        self.balance - amount

class SavingsAccount(BankAccount):
    def __init__(self, balance, min_balance):
        super().__init__(balance)
        self.min_balance = min_balance
    
    def withdraw(self, amount):
        if self.balance - amount < self.min_balance:
            raise ValueError("Not enough balance")
        self.balance - amount


def main():
    bank_account = BankAccount(100)
    bank_account.deposit(50)
    bank_account.withdraw(20)
    print(f"Balance: {bank_account.balance}")
    
    savings_account = SavingsAccount(100, 50)
    savings_account.deposit(50)
    savings_account.withdraw(20)
    print(f"Balance: {savings_account.balance}")

if __name__ == "__main__":
    main()