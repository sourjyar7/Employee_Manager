from employee_manager.db.retrieve_employees import EmployeesRetriever
from employee_manager.utils.employee_validator_schema import EmployeeDbSchema
from flask import jsonify

class EmployeesFetcher():
    
    def fetch_employee(self):
        employees_retriever=EmployeesRetriever()
        result=employees_retriever.retrieve_employees()
        employee_db_schema=EmployeeDbSchema(many=True)
        result=employee_db_schema.dump(result)
        return jsonify(result)   