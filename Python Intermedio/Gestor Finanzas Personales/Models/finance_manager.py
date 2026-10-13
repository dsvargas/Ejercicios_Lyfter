import json
import os
from typing import List
from Models.transaction import Transaction, Expense, Income


class Finance_manager:

    def __init__(self, file_path: str = "finance_data.json"):
        self.file_path = file_path
        self.categories: List[str] = []
        self.movements: List[Transaction] = []
        self.load_data()  # Carga los datos guardados en disco al instanciar

    def add_category(self, category_name: str) -> bool:
        category_clean = category_name.strip().lower()
        if category_clean and category_clean not in self.categories:
            self.categories.append(category_clean)
            self.save_data()
            return True
        return False

    def add_movement(self, movement: Transaction):
        # Validar título
        if not movement.title or not movement.title.strip():
            raise ValueError("El título de la transacción no puede estar vacío.")

        # Validar monto
        try:
            amount_val = float(movement.amount)
            if amount_val <= 0:
                raise ValueError("El monto debe ser un valor numérico positivo mayor a cero.")
        except (TypeError, ValueError):
            raise ValueError("El monto ingresado no es un número válido.")

        # Asignar un ID incremental básico si no existe
        if movement.transaction_id is None:
            movement.transaction_id = len(self.movements) + 1

        self.movements.append(movement)
        self.save_data()

    def get_balance(self) -> float:
        total_income = sum(
            m.amount for m in self.movements if isinstance(m, Income)
        )
        total_expense = sum(
            m.amount for m in self.movements if isinstance(m, Expense)
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

                # Validamos que el JSON tenga la estructura esperada
                if not isinstance(data, dict):
                    raise ValueError("El archivo JSON no tiene un formato de diccionario válido.")

                self.categories = data.get("categories", [])
                self.movements = []

                for item in data.get("movements", []):
                    m_type = item.get("type")
                    if m_type == "Expense":
                        mov = Expense(
                            title=item["title"],
                            amount=item["amount"],
                            category=item["category"],
                            description=item.get("description", ""),
                            movement_date=item.get("date", ""),
                            transaction_id=item.get("transaction_id"),
                        )
                        self.movements.append(mov)
                    elif m_type == "Income":
                        mov = Income(
                            title=item["title"],
                            amount=item["amount"],
                            category=item["category"],
                            description=item.get("description", ""),
                            movement_date=item.get("date"),
                            transaction_id=item.get("transaction_id"),
                        )
                        self.movements.append(mov)
        except json.JSONDecodeError:
            return "El archivo de datos está corrupto o tiene un formato JSON inválido."
        except PermissionError:
            return "No hay permisos de lectura para acceder al archivo de datos."
        except (KeyError, TypeError, ValueError) as e:
            return f"La estructura de los datos en el archivo está dañada: {e}"