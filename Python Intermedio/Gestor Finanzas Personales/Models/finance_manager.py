import json
import os
from typing import List
from Models.transaction import Transaction, Expense, Income
from pathlib import Path

class FinanceManager:

    def __init__(self, file_path: str = "finance_data.json"):
        # Subimos dos niveles (.parent.parent) si estamos dentro de Models/ 
        # para que el archivo JSON quede en la raíz del proyecto.
        base_dir = Path(__file__).resolve().parent.parent
        
        # Si se pasa la ruta por defecto o una personalizada, se gestiona con Path
        if file_path == "finance_data.json":
            self.file_path = base_dir / file_path
        else:
            self.file_path = Path(file_path)

        self.categories: List[str] = []
        self.movements: List[Transaction] = []
        self.load_data()  # Carga los datos guardados en disco al instanciar
        self.load_error = self.load_data()  # Guarda el error si ocurre, en lugar de ignorarlo

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

            # Mapeo de texto del JSON a la clase correspondiente
            class_mapping = {
                "Expense": Expense,
                "Income": Income
            }

            for item in data.get("movements", []):
                m_type = item.get("type")
                
                # Verificamos si la clase existe en nuestro mapeo
                if m_type in class_mapping:
                    movement_class = class_mapping[m_type]
                    
                    mov = movement_class(
                        title=item["title"],
                        amount=item["amount"],
                        category=item["category"],
                        description=item.get("description", ""),
                        movement_date=item.get("date", ""),
                        transaction_id=item.get("transaction_id"),
                    )
                    self.movements.append(mov)

        except json.JSONDecodeError:
            # Respalda el archivo dañado para evitar perder la información del usuario
            if self.file_path.exists():
                backup_path = self.file_path.with_name("finance_data_corrupted.json")
                self.file_path.rename(backup_path)
            return "El archivo de datos está corrupto. Se ha respaldado como 'finance_data_corrupted.json'."
        except PermissionError:
            return "No hay permisos de lectura para acceder al archivo de datos."
        except (KeyError, TypeError, ValueError) as e:
            return f"La estructura de los datos en el archivo está dañada: {e}"