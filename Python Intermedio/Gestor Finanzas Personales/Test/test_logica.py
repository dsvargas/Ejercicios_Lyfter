import os
import pytest
from Models.finance_manager import Finance_manager as Finance_manager
from Models.transaction import Expense, Income, Transaction as Movement


@pytest.fixture
def temp_manager(tmp_path):
    """Creates a temporary FinanceManager with an isolated JSON file."""
    db_file = tmp_path / "test_finance.json"
    return Finance_manager(file_path=str(db_file))


def test_movement_inheritance():
    """Verify polymorphic behavior and subclassing."""
    exp = Expense("Lunch", 15.50, "Food")
    inc = Income("Salary", 1000.00, "Work")

    assert isinstance(exp, Movement)
    assert isinstance(inc, Movement)
    assert exp.get_movement_type() == "Expense"
    assert inc.get_movement_type() == "Income"


def test_balance_calculation(temp_manager):
    """Verify balance calculation with Expenses and Incomes."""
    temp_manager.add_movement(Income("Freelance", 500.0, "Work"))
    temp_manager.add_movement(Expense("Groceries", 150.0, "Food"))

    assert temp_manager.get_balance() == 350.0


def test_category_management(temp_manager):
    """Verify category addition and duplicate prevention."""
    assert temp_manager.add_category("Entertainment") is True
    assert temp_manager.add_category("Entertainment") is False  # Duplicate
    assert "Entertainment" in temp_manager.categories


def test_transaction_to_dict():
    """Verify that Transaction's to_dict method returns the correct dictionary."""
    transaction = Movement(
        "Book Purchase", 20.0, "Education", "Bought a book", "2024-06-01", 1
    )
    expected_dict = {
        "type": "Transaction",
        "transaction_id": 1,
        "title": "Book Purchase",
        "amount": 20.0,
        "category": "Education",
        "description": "Bought a book",
        "date": "2024-06-01",
    }
    assert transaction.to_dict() == expected_dict


def test_transaction_repr():
    """Verify that the __repr__ method returns the expected string representation."""
    transaction = Movement("Gym Membership", 30.0, "Health")
    expected_repr = "Transaction(Gym Membership, 30.0, Health)"
    assert repr(transaction) == expected_repr


def test_transaction_id_assignment(temp_manager):
    """Verify that transaction IDs are assigned correctly when adding movements."""
    inc = Income("Investment", 1000.0, "Finance")
    exp = Expense("Utilities", 200.0, "Bills")

    temp_manager.add_movement(inc)
    temp_manager.add_movement(exp)

    assert inc.transaction_id is not None
    assert exp.transaction_id is not None
    assert inc.transaction_id != exp.transaction_id

def test_load_data_invalid_structure(tmp_path):
    """Verify that loading a JSON with invalid internal structure (e.g. a list instead of a dict) returns an error."""
    invalid_file = tmp_path / "invalid_structure.json"
    # Escribimos un JSON válido sintácticamente, pero que estructuralmente es una lista en vez de un diccionario
    invalid_file.write_text(json.dumps(["not", "a", "dictionary"]), encoding="utf-8")

    manager = FinanceManager(file_path=str(invalid_file))
    error_message = manager.load_data()

    assert error_message is not None
    assert "formato" in error_message.lower() or "diccionario" in error_message.lower()
    assert manager.movements == []
    assert manager.categories == []