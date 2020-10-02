from employee_manager import db
from employee_manager.db.models import Project

class ProjectSaver:
    project=None
    
    def __init__(self,project):
        self.project=project 
    
    def save(self):
        try:
           db.session.add(self.project)
           db.session.commit()
           return True
        except Exception as err:
           return False 