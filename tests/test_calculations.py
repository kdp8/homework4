'''My Calculator Test'''
from decimal import Decimal
import pytest
from calculator.calculation import Calculation
from calculator.calculations import Calculations

from calculator.operations import add, subtract

@pytest.fixture
def setup_calculations():
    """Fixture to set up initial calculations for testing."""
    Calculations.clear_history()
    Calculations.add_calculation(Calculation(Decimal('10'), Decimal('5'), add))
    Calculations.add_calculation(Calculation(Decimal('20'), Decimal('3'), subtract))

def test_add_calculation(setup_calculations):
    """Test adding a calculation to the history."""
    calc = Calculation(Decimal('2'), Decimal('2'), add)
    Calculations.add_calculation(calc)
    assert Calculations.get_latest() == calc, "Failed to add the calculation to history"

def test_get_history(setup_calculations):
    """Test getting the calculation history."""
    history = Calculations.get_history()
    assert len(history) == 2, "The number of calculations in History does not match"

def test_clear_history(setup_calculations):
    """Test clearing the calculation history."""
    Calculations.clear_history()
    assert len(Calculations.get_history()) == 0, "History not cleared"

def test_get_latest(setup_calculations):
    """Test retrieving the latest calculation."""
    latest = Calculations.get_latest()
    assert latest.a == Decimal('20') and latest.b == Decimal('3'), "Failed to get the correct latest calculation"

def test_find_by_operation(setup_calculations):
    """Test finding calculations by operation."""
    add_operations = Calculations.find_by_operation("add")
    assert len(add_operations) == 1, "Failed to find the correct number of calculations with add operation"
    subtract_operations = Calculations.find_by_operation("subtract")
    assert len(subtract_operations) == 1, "Failed to find the correct number of calculations with subtract operation"

def test_get_latest_with_empty_history():
    """Test retrieving the latest calculation from an empty history."""
    Calculations.clear_history()
    assert Calculations.get_latest() is None, "Expected None for the latest calculation with empty history"
