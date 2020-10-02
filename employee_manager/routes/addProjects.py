from flask import jsonify,Blueprint,request
from employee_manager.middleware.employee_validator import validate_details
from employee_manager.services.add_project_service import ProjectAdder


add_projects=Blueprint('add_projects',__name__)

@add_projects.route('/addProjects',methods=['POST'])
def add():
    count=0
    for project in request.json:
        project_adder=ProjectAdder(project)
        if project_adder.add_project():
            count=count+1
    
    return jsonify({"msg":f"added {count} out of {len(request.json)} projects"}),200