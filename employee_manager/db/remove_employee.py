from employee_manager.db.models import Employee
from employee_manager import db

class EmployeeRemover:
    id=None
    def __init__(self,id):
        self.id=id

    def remove_employee(self):
        try:
            if Employee.query.filter_by(eid=self.id).first() == None:
                return "No employee with given id found"
            Employee.query.filter_by(eid=self.id).delete()
            db.session.commit()
            return "succesfully removed"
        except Exception:
            return "failure"    