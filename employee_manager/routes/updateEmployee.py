from flask import jsonify,Blueprint,request
from employee_manager.middleware.employee_validator import validate_details
from employee_manager.services.update_employee_service import EmployeeUpdater
update_employee=Blueprint('update_employee',__name__)

@update_employee.route('/updateEmployee/<id>',methods=['PUT'])
@validate_details
def update(id):
    employee={}
    departments=request.json["departments"]
    employee["firstname"]=request.json["firstname"]
    employee["lastname"]=request.json["lastname"]
    employee["email"]=request.json["email"]
    employee["mobile_no"]=request.json["mobile_no"]
    employee["doj"]=request.json["doj"]
    employ_updater=EmployeeUpdater(id,employee,departments)
    return employ_updater.update_employee()