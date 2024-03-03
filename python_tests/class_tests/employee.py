#!/usr/bin/python3

class Employee:
    """Representing an employee"""

    def __init__(self, first_name, last_name, annual_salary):
        """Initializing class attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary

    def give_raise(self, salary_raise=5000):
        """Give employee a raise"""
        self.annual_salary += salary_raise
        print(f"The new salary is {self.annual_salary}!")