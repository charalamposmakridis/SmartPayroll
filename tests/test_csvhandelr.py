import unittest

from model.employee import Employee
from storage.csvhandler import CSVHandler
import os


class TestCSVHandler(unittest.TestCase):
    def setUp(self):
        self.filepath="data/payroll.csv"
        self.csvhandler=CSVHandler(self.filepath)

    def tearDown(self):
        if os.path.exists(self.filepath):
            os.remove(self.filepath)

    def test_save_employee(self):
        emp=Employee(
            emp_id=1,
            fullname="Makridhs Xaralampos",
            department="IT",
            base_salary=1200.0,
            overtime_hours=10.0,
            hourly_rate=20.0
        )

        self.csvhandler.save_employee(emp.to_dict())
        result=self.csvhandler.load_all_employees()

        self.assertEqual(len(result),1)
        self.assertEqual(result[0].fullname,"Makridhs Xaralampos")

    def test_delete_employee(self):
        emp=Employee(1,"Test User","HR",1000.0,0,0)
        self.csvhandler.save_employee(emp.to_dict())

        result=self.csvhandler.delete_employee(1)

        all_emps=self.csvhandler.load_all_employees()
        self.assertTrue(result)
        self.assertEqual(len(all_emps),0)

    def test_update_employee(self):
        emp=Employee(1,"Original Name","IT",1000.0,0,0)
        self.csvhandler.save_employee(emp.to_dict())

        updated_emp=Employee(1,"Updated Name","IT",1500.0,5.0,20.0)
        result=self.csvhandler.update_employee(updated_emp)

        all_emps = self.csvhandler.load_all_employees()
        self.assertTrue(result)
        self.assertEqual(all_emps[0].fullname, "Updated Name")
        self.assertEqual(all_emps[0].base_salary, 1500.0)

    def test_auto_increment_id(self):
        emp1=Employee(0,"First","IT",1000.0,0,0)
        emp2=Employee(0,"Second","IT",1000.0,0,0)

        id1=self.csvhandler.save_employee(emp1.to_dict())
        id2=self.csvhandler.save_employee(emp2.to_dict())

        self.assertEqual(id1,1)
        self.assertEqual(id2,2)

if __name__=='__main__':
    unittest.main()
