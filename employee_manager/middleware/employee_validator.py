from functools import wraps
from employee_manager.utils.employee_validator_schema import EmployeeInputSchema
from flask import request,jsonify
from marshmallow import ValidationError

def validate_details(func):
    @wraps(func)
    def decorator(*args,**kwargs):
        print("validator running")
        employee_schema=EmployeeInputSchema()
        employee={}
        employee["firstname"]=request.json["firstname"]
        employee["lastname"]=request.json["lastname"]
        employee["email"]=request.json["email"]
        employee["mobile_no"]=request.json["mobile_no"]
        employee["doj"]=request.json["doj"]
        try:
          employee_schema.load(employee)
          return func(*args,**kwargs)
        except ValidationError as err:
          print(err.messages) 
          return jsonify({'error':err.messages}),400   
        
    return decorator        