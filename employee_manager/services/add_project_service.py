from employee_manager.db.models import Project
from employee_manager.db.save_project import ProjectSaver 

class ProjectAdder:
    project=None
   
    def __init__(self,project):
        self.project=project  
    
    def add_project(self):
        if len(Project.query.filter_by(name=self.project['proj']).all()) == 0:
            project_data=Project(self.project['proj'])
            project_saver=ProjectSaver(project_data)
            return project_saver.save()
        else:
            return False 