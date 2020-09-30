from employee_manager.db.modify_employee import EmployeeModifier
from flask import jsonify

class EmployeeUpdater():
    id=None
    updated_employee=None

    def __init__(self,id,updated_employee):
        self.id=id
        self.updated_employee=updated_employee

    def update_employee(self):
        employee_modifier=EmployeeModifier(self.id,self.updated_employee)
        return jsonify({'msg': employee_modifier.modify_employee()})    