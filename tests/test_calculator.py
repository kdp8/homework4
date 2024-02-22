'''My Calculator Test'''
from faker import Faker
from calculator import Calculator

fake = Faker()

def test_addition():
    '''Test that addition function works '''    
    a = fake.random_number(digits=2)
    b = fake.random_number(digits=2)
    expected = a + b
    assert Calculator.add(a, b) == expected

def test_subtraction():
    '''Test that subtraction function works '''    
    a = fake.random_number(digits=2)
    b = fake.random_number(digits=2)
    expected = a - b
    assert Calculator.subtract(a, b) == expected

def test_divide():
    '''Test that division function works '''    
    a = fake.random_number(digits=2)
    b = fake.random_number(digits=2)
    if b == 0:
        b = 1
    expected = a / b
    assert Calculator.divide(a, b) == expected

def test_multiply():
    '''Test that multiply function works '''    
    a = fake.random_number(digits=2)
    b = fake.random_number(digits=2)
    expected = a * b
    assert Calculator.multiply(a, b) == expected
