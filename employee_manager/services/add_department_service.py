from employee_manager.db.models import Department
from employee_manager.db.save_department import DepartmentSaver 

class DepartmentAdder:
    department=None
   
    def __init__(self,department):
        self.department=department  
    
    def add_department(self):
        if len(Department.query.filter_by(name=self.department['dept']).all()) == 0:
            department_data=Department(self.department['dept'])
            department_saver=DepartmentSaver(department_data)
            return department_saver.save()
        else:
            return False    