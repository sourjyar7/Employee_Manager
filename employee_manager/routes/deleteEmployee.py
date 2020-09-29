from flask import jsonify,Blueprint
from employee_manager.middleware.validator import validate_details

delete_employee = Blueprint('delete_employee',__name__)

@delete_employee.route('/deleteEmployee',methods=['DELETE'])
@validate_details
def delete():
    return jsonify({'msg':'deleteEmployee'})

