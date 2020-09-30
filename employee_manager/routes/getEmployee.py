from flask import jsonify,Blueprint
from employee_manager.services.get_employee_service import EmployeeFetcher

get_employee=Blueprint('get_employee',__name__)

@get_employee.route('/getEmployee/<id>',methods=['GET'])
def get(id):
    if id.isnumeric():
        if int(id) <= 0:
            return jsonify({'error':'invalid id !'}),400
        else:
            employee_fetcher=EmployeeFetcher(id)
            return employee_fetcher.fetch_employee(),200
    else:
        return jsonify({'error':'invalid id !'}),400
