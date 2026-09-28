import json
import os
from typing import List
from Models.transaction import Transaction, expense, income


class finance_manager:

    def __init__(self, file_path: str = "finance_data.json"):
        self.file_path = file_path
        self.categories: List[str] = []
        self.movements: List[Transaction] = []
        self.load_data()  # Carga los datos guardados en disco al instanciar

    def add_category(self, category_name: str) -> bool:
        category_clean = category_name.strip()
        if category_clean and category_clean not in self.categories:
            self.categories.append(category_clean)
            self.save_data()
            return True
        return False

    def add_movement(self, movement: Transaction):
        # Asignar un ID incremental básico si no existe
        if movement.transaction_id is None:
            movement.transaction_id = len(self.movements) + 1

        self.movements.append(movement)
        self.save_data()

    def get_balance(self) -> float:
        total_income = sum(
            m.amount for m in self.movements if isinstance(m, income)
        )
        total_expense = sum(
            m.amount for m in self.movements if isinstance(m, expense)
        )
        return total_income - total_expense

    def save_data(self):
        """Guarda categorías y transacciones en el archivo JSON."""
        data = {
            "categories": self.categories,
            "movements": [m.to_dict() for m in self.movements],
        }
        with open(self.file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

    def load_data(self):
        """Lee el archivo JSON y reconstruye los objetos en memoria."""
        if not os.path.exists(self.file_path):
            return

        try:
            with open(self.file_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                self.categories = data.get("categories", [])
                self.movements = []

                for item in data.get("movements", []):
                    m_type = item.get("type")
                    if m_type == "Expense":
                        mov = expense(
                            title=item["title"],
                            amount=item["amount"],
                            category=item["category"],
                            description=item.get("description", ""),
                            date=item.get("date", ""),
                            transaction_id=item.get("transaction_id"),
                        )
                        self.movements.append(mov)
                    elif m_type == "Income":
                        mov = income(
                            title=item["title"],
                            amount=item["amount"],
                            category=item["category"],
                            description=item.get("description", ""),
                            date=item.get("date", ""),
                            transaction_id=item.get("transaction_id"),
                        )
                        self.movements.append(mov)
        except Exception as e:
            print(f"Error al cargar datos desde {self.file_path}: {e}")
            self.categories = []
            self.movements = []