from employee_manager import db
from employee_manager.db.models import Department

class EmployeeSaver:
    employee=None
    departments=None

    def __init__(self,employee,departments):
        self.employee=employee 
        self.departments=departments
    
    def save(self):
        try:
            for dept in self.departments:
                self.employee.departments.append(Department(dept))
            
            db.session.add(self.employee)
            db.session.commit()
            return "success"
        except Exception as err:
            return "failure"      