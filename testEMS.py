import unittest
from EMS import EMS,Employee

class TestEMS(unittest.TestCase):
    def test_add(self):
        ems = EMS()
        employee = Employee("Peter Parker",23,69,"WebSlinger")
        ems.add_emp(employee)
        self.assertIn(employee,ems.data)

    def test_show(self):
        ems = EMS()
        ems.add_emp(Employee("Peter Parker",23,69,"WebSlinger"))
        ems.add_emp(Employee("Kraven",36,70,"Hunter"))
        ems.add_emp(Employee("Miles Morales",19,71,"WebSlinger Intern"))

        print('/////')
        expected_output = "Peter Parker 69 23 WebSlinger\nKraven 70 36 Hunter\nMiles Morales 71 19 WebSlinger Intern\n"
        output = self.get_output_string(ems.show_employees)

        print(expected_output)

        print(output)

        self.assertEqual(expected_output,output)

    
    def get_output_string(self, func):
        import io
        from contextlib import redirect_stdout
        f = io.StringIO()
        with redirect_stdout(f):
            func()
        return f.getvalue()