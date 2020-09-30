from employee_manager import ma
from employee_manager.db.models import Employee
from marshmallow import fields,validate,Schema

class EmployeeInputSchema(Schema):
    firstname=fields.String(required=True)
    lastname=fields.String(required=True)
    department=fields.String(required=True)
    email=fields.Email(required=True)
    mobile_no=fields.String(required=True,validate=validate.Length(10))
    doj=fields.Date(required=True)
    class Meta:
        ma.fields=('eid','firstname','lastname','department','email','mobile_no','doj')

class EmployeeDbSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model=Employee
        ma.fields=('eid','firstname','lastname','department','email','mobile_no','doj')
