from employee_manager import db
from employee_manager.db.models import Department

class DepartmentSaver:
    department=None
    
    def __init__(self,department):
        self.department=department 
    
    def save(self):
        try:
           db.session.add(self.department)
           db.session.commit()
           return True
        except Exception as err:
           return False 
       