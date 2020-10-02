from flask import jsonify,Blueprint,request
from employee_manager.middleware.employee_validator import validate_details
from employee_manager.services.add_employee_service import EmployeeAdder


add_employee=Blueprint('add_employee',__name__)

@add_employee.route('/addEmployee',methods=['POST'])
@validate_details
def add():
    employee={}
    employee["firstname"]=request.json["firstname"]
    employee["lastname"]=request.json["lastname"]
    employee["email"]=request.json["email"]
    employee["mobile_no"]=request.json["mobile_no"]
    employee["doj"]=request.json["doj"]
    employee_adder=EmployeeAdder(employee)
    return jsonify({'msg': employee_adder.add_employee()}),200