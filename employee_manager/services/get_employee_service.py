from employee_manager.db.retrieve_employee import EmployeeRetriever
from employee_manager.utils.employee_validator_schema import EmployeeDbSchema
from flask import jsonify

class EmployeeFetcher():
    id=None
    def __init__(self,id):
        self.id=id

    def fetch_employee(self):
        employee_retriever=EmployeeRetriever(self.id)
        result=employee_retriever.retrieve_employee()
        employee_db_schema=EmployeeDbSchema()
        result=employee_db_schema.dump(result)
        return jsonify(result)   