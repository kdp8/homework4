"""
Calculator Module

This module provides basic arithmetic operations using the Decimal class.
"""

from decimal import Decimal
import pytest
from calculator.calculation import Calculation
from calculator.operations import add, subtract, multiply, divide

def test_operation_add():
    """
    Test the addition operation of the calculator.
    """
    calculation = Calculation(Decimal('10'), Decimal('5'), add)
    assert calculation.perform() == Decimal('15'), "Add operation failed"

def test_operation_subtract():
    """
    Test the subtraction operation of the calculator.
    """
    calculation = Calculation(Decimal('10'), Decimal('5'), subtract)
    assert calculation.perform() == Decimal('5'), "Subtraction operation failed"

def test_operation_multiply():
    """
    Test the multiplication operation of the calculator.
    """
    calculation = Calculation(Decimal('10'), Decimal('5'), multiply)
    assert calculation.perform() == Decimal('50'), "Multiplication operation failed"

def test_operation_divide():
    """
    Test the division operation of the calculator.
    """
    calculation = Calculation(Decimal('10'), Decimal('5'), divide)
    assert calculation.perform() == Decimal('2'), "Division operation failed"

def test_operation_divide_by_zero():
    """
    Test the division operation when dividing by zero.
    """
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calculation = Calculation(Decimal('10'), Decimal('0'), divide)
        calculation.perform()
