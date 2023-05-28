import unittest
from EMS import EMS,Employee

class TestEMS(unittest.TestCase):
     #testing employee management system
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


        expected_output = "Peter Parker 69 23 WebSlinger\nKraven 70 36 Hunter\nMiles Morales 71 19 WebSlinger Intern\n"
        output = self.get_output_string(ems.show_employees)

        self.assertEqual(expected_output,output)

    def test_delete(self):
        ems = EMS()
        emp1 = Employee("Peter Parker",23,69,"WebSlinger")
        emp2 = Employee("Kraven",36,70,"Hunter")
        emp3 = Employee("Miles Morales",19,71,"WebSlinger Intern")

        ems.add_emp(emp1)
        ems.add_emp(emp2)
        ems.add_emp(emp3)

        ems.delete_employee(69)

        self.assertNotIn(emp1,ems.data)

    def test_delete_not_found(self):
        ems = EMS()
        emp1 = Employee("Peter Parker",23,69,"WebSlinger")
        emp2 = Employee("Kraven",36,70,"Hunter")
        emp3 = Employee("Miles Morales",19,71,"WebSlinger Intern")

        ems.add_emp(emp1)
        ems.add_emp(emp2)
        ems.add_emp(emp3)        

        with self.assertRaises(Exception):
            ems.delete_employee(68)


    
    def get_output_string(self, func):
        import io
        from contextlib import redirect_stdout
        f = io.StringIO()
        with redirect_stdout(f):
            func()
        return f.getvalue()