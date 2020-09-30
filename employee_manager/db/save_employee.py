import employee_manager

class EmployeeSaver:
    employee=None
    
    def __init__(self,employee):
        self.employee=employee 
    
    def save(self):
        employee_manager.db.session.add(self.employee)
        employee_manager.db.session.commit()
        return "success"  