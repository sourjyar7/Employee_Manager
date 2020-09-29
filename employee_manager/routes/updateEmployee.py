from flask import jsonify,Blueprint
from employee_manager.middleware.validator import validate_details

update_employee=Blueprint('update_employee',__name__)

@update_employee.route('/updateEmployee',methods=['PUT'])
@validate_details
def update():
    return jsonify({'msg':'updateEmployee'})
