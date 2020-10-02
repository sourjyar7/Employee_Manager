from flask import jsonify,Blueprint,request
from employee_manager.middleware.employee_validator import validate_details
from employee_manager.services.add_department_service import DepartmentAdder


add_departments=Blueprint('add_departments',__name__)

@add_departments.route('/addDepartments',methods=['POST'])
def add():
    count=0
    for department in request.json:
        department_adder=DepartmentAdder(department)
        if department_adder.add_department():
            count=count+1
    
    return jsonify({"msg":f"added {count} out of {len(request.json)} departments"}),200