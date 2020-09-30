from flask import jsonify,Blueprint
from employee_manager.middleware.employee_validator import validate_details

get_employee=Blueprint('get_employee',__name__)

@get_employee.route('/getEmployee',methods=['GET'])
@validate_details
def get():
    return jsonify({'msg':'getEmployee'})
