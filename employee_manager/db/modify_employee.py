from employee_manager.db.models import Employee
from employee_manager import db

class EmployeeModifier:
    id=None
    updated_employee=None

    def __init__(self,id,updated_employee):
        self.id=id
        self.updated_employee=updated_employee

    def modify_employee(self):
        try:
            tobemod_employee=Employee.query.filter_by(eid=self.id).first()
            tobemod_employee.firstname=self.updated_employee['firstname'];
            tobemod_employee.lastname=self.updated_employee['lastname'];
            tobemod_employee.department=self.updated_employee['department'];
            tobemod_employee.email=self.updated_employee['email'];
            tobemod_employee.mobile_no=self.updated_employee['mobile_no'];
            tobemod_employee.doj=self.updated_employee['doj'];
            db.session.commit()
            return "succesfully updated"
        except Exception:
            return "failed to update"
        