from employee_manager.db.models import Employee
from employee_manager.db.save_employee import EmployeeSaver 

class EmployeeAdder:
    employee=None
   
    def __init__(self,employee):
        self.employee=employee  
    
    def add_employee(self):
        employee_data=Employee(self.employee["firstname"],self.employee["lastname"],self.employee["email"],self.employee["mobile_no"],self.employee["doj"])
        employee_saver=EmployeeSaver(employee_data)
        return  employee_saver.save()


        




