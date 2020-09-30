from flask import jsonify,Blueprint
from employee_manager.middleware.employee_validator import validate_details
from employee_manager.services.delete_employee_service import EmployeeDeleter

delete_employee = Blueprint('delete_employee',__name__)

@delete_employee.route('/deleteEmployee/<id>',methods=['DELETE'])
@validate_details
def delete(id):
    if id.isnumeric():
        if int(id) <= 0:
            return jsonify({'error':'invalid id !'}),400
        else:
            employee_deleter=EmployeeDeleter(id)
            return employee_deleter.delete_employee(),200
    else:
        return jsonify({'error':'invalid id !'}),400

