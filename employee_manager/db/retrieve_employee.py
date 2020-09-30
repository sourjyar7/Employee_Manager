from employee_manager.db.models import Employee

class EmployeeRetriever:
    id=None
    def __init__(self,id):
        self.id=id

    def retrieve_employee(self):
        try:
            employee=Employee.query.filter_by(eid=self.id).first()
            return employee
        except Exception:
            return "failure"        
          
    