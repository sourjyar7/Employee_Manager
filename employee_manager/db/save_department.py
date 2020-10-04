from employee_manager import db
from employee_manager.db.models import Department
from employee_manager.db.models import Project

class DepartmentSaver:
    department=None
    projects=None
    
    def __init__(self,department,projects):
        self.department=department 
        self.projects=projects
    
    def save(self):
        try:
           for project in self.projects:
               if len(Project.query.filter_by(name=project).all()) == 0:
                   self.department.projects.append(Project(project)) 
               else:
                   proj=Project.query.filter_by(name=project).one()
                   self.department.projects.append(proj)

           
           db.session.add(self.department)
           db.session.commit()
           return True
        except Exception as err:
           return False 
       