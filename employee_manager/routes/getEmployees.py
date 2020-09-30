from flask import jsonify,Blueprint
from employee_manager.services.get_employees_service import EmployeesFetcher

get_employees=Blueprint('get_employees',__name__)

@get_employees.route('/getEmployees',methods=['GET'])
def get():
    employee_fetcher=EmployeesFetcher()
    return employee_fetcher.fetch_employee(),200