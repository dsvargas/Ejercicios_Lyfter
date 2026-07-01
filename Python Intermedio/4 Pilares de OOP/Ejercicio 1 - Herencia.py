'''Cree una clase de BankAccount que:

    Tenga un atributo de balance.
    Tenga un método para ingresar dinero.
    Tengo un método para retirar dinero.
    Cree otra clase que herede de esta llamada SavingsAccount que:
    Tenga un atributo de min_balance que se pueda asignar al crearla.
    Arroje un error si al intentar retirar dinero, el retiro haría que el balance quede debajo del min_balance. Es decir que sí se pueden hacer retiros siempre y cuando el balance quede arriba del min_balance.
'''

class BankAccount:
    def __init__(self):
        self.balance = 0

    def add_money(self, amount):
        self.balance += amount

    def witdraw_money(self, amount):
        self.balance -= amount

class SavingsAccount(BankAccount):
    def __init__(self, initial_balance, min_balance):
        super().__init__()
        self.balance = initial_balance
        self.min_balance = min_balance

    def witdraw_money(self, amount):
        simulated_balance = self.balance - amount

        if self.min_balance <= simulated_balance:
            super().witdraw_money(amount)
            print(f"Retiro exitoso de ₡{amount:.2f}. Nuevo saldo: ₡{self.balance:.2f}")
            return True
        else:
            print(f"Error de Retiro: No puede dejar la cuenta por debajo del saldo mínimo permitido (₡{self.min_balance:.2f}).")
            print(f"   Saldo actual: ₡{self.balance:.2f} | Intento de retiro: ₡{amount:.2f} (Faltarían ₡{abs(simulated_balance - self.min_balance):.2f})")
            return False
        
cuenta = SavingsAccount(1000, 300)
    
cuenta.witdraw_money(500)
print("-" * 40)
cuenta.witdraw_money(400)
print("-" * 40)
cuenta.add_money(200)
cuenta.witdraw_money(300)