from functools import wraps
from employee_manager.utils.employee_validator_schema import EmployeeInputSchema
from flask import request,jsonify
from marshmallow import ValidationError

def validate_details(func):
    @wraps(func)
    def decorator(*args,**kwargs):
        print("validator running")
        employee_schema=EmployeeInputSchema()
        try:
          employee_schema.load(request.json)
          return func(*args,**kwargs)
        except ValidationError as err:
          print(err.messages) 
          return jsonify({'error':err.messages}),400   
        
    return decorator        