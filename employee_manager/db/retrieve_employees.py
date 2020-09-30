from employee_manager.db.models import Employee

class EmployeesRetriever:
    
    def retrieve_employees(self):
        try:
            employees=Employee.query.all()
            return employees
        except Exception:
            return "failure"        
          