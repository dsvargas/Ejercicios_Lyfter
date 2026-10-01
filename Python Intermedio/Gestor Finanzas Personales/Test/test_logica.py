import os
import pytest
from Models.finance_manager import Finance_manager as Finance_manager
from Models.transaction import (
    Transaction as Movement,
    expense as Expense,
    income as Income,
)


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


def test_income_deposit(temp_manager):
    """Verify that depositing income updates the account balance correctly."""
    account = temp_manager
    initial_balance = account.get_balance()

    # Usamos el alias Income e ingresamos el movimiento a través del gestor
    new_income = Income("Bonus", 200.0, "Work")
    account.add_movement(new_income)

    assert account.get_balance() == initial_balance + 200.0


def test_expense_withdraw(temp_manager):
    """Verify that withdrawing expense updates the account balance correctly."""
    account = temp_manager
    initial_balance = account.get_balance()

    # Usamos el gestor para registrar el gasto
    new_expense = Expense("Dinner", 50.0, "Food")
    account.add_movement(new_expense)

    assert account.get_balance() == initial_balance - 50.0


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