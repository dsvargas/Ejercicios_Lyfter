from datetime import date
class Transaction:

    def __init__(
        self,
        title: str,
        amount: float,
        category: str,
        description: str = "",
        movement_date = None,
        transaction_id: int = None,
    ):
        self.transaction_id = transaction_id
        self.amount = float(amount)
        # Aseguramos que se asigne la fecha actual si no viene una guardada
        self.date = movement_date if movement_date else date.today().strftime("%Y-%m-%d")
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
        return f"Transaction({self.title}, {self.amount}, {self.category}, {self.date})"


class Income(Transaction):

    def get_movement_type(self) -> str:
        return "Income"

class Expense(Transaction):

    def get_movement_type(self) -> str:
        return "Expense"