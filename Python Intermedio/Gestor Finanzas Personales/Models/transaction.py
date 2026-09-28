class Transaction:

    def __init__(
        self,
        title: str,
        amount: float,
        category: str,
        description: str = "",
        date: str = "",
        transaction_id: int = None,
    ):
        self.transaction_id = transaction_id
        self.amount = float(amount)
        self.date = date
        self.title = title
        self.description = description
        self.category = category

    def get_movement_type(self) -> str:
        return "Transaction"

    def to_dict(self) -> dict:
        """Convierte la instancia a un diccionario para guardarla en JSON."""
        return {
            "type": self.get_movement_type(),
            "transaction_id": self.transaction_id,
            "title": self.title,
            "amount": self.amount,
            "category": self.category,
            "description": self.description,
            "date": self.date,
        }

    def __repr__(self):
        return f"Transaction({self.title}, {self.amount}, {self.category})"


class income(Transaction):

    def get_movement_type(self) -> str:
        return "Income"

    def deposit(self, account):
        account.balance += self.amount
        print(
            f"Deposited {self.amount} to account. New balance: {account.balance}"
        )


class expense(Transaction):

    def get_movement_type(self) -> str:
        return "Expense"

    def withdraw(self, account):
        account.balance -= self.amount
        print(
            f"Withdrew {self.amount} from account. New balance: {account.balance}"
        )