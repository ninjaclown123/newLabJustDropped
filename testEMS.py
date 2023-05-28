import unittest
from EMS import EMS,Employee

class TestEMS(unittest.TestCase):
    def test_add(self):
        ems = EMS()
        employee = Employee("Peter Parker",23,69,"WebSlinger")
        ems.add_emp(employee)
        self.assertIn(employee,ems.data)