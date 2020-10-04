from employee_manager.db.models import Department
from employee_manager.db.save_department import DepartmentSaver 

class DepartmentAdder:
    department=None
    projects=None
   
    def __init__(self,department,projects):
        self.department=department  
        self.projects=projects
    
    def add_department(self):
        if len(Department.query.filter_by(name=self.department).all()) == 0:
            department_data=Department(self.department)
            department_saver=DepartmentSaver(department_data,self.projects)
            return department_saver.save()
        else:
            return False    