from employee_manager.db.remove_employee import EmployeeRemover
from employee_manager.utils.employee_validator_schema import EmployeeDbSchema
from flask import jsonify

class EmployeeDeleter:
    id=None

    def __init__(self,id):
        self.id=id
    
    def delete_employee(self):
        employee_remover=EmployeeRemover(self.id)
        return jsonify({'msg': employee_remover.remove_employee()})