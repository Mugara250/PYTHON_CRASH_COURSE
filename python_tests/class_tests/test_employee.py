#!/usr/bin/python3
import pytest
from employee import Employee

@pytest.fixture
def employee():
    """An employee that can be applied to all test functions"""
    employee = Employee('Boris', 'Nyilindekwe', 6000)
    return employee
def test_give_default_raise(employee):
    """Test whether the salary raise is 5000 by default"""
    employee.give_raise()
    assert employee.annual_salary == 11000

def test_give_custom_raise(employee):
    """Test whether the salary can be raised with a different amount"""
    employee.give_raise(4000)
    assert employee.annual_salary == 10000