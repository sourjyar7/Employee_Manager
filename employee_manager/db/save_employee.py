from employee_manager import db

class EmployeeSaver:
    employee=None
    
    def __init__(self,employee):
        self.employee=employee 
    
    def save(self):
        db.session.add(self.employee)
        db.session.commit()
        return "success"  