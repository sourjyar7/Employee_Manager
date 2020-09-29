from flask import Flask,request,jsonify
from employee_manager.db.db_connector import db_connector

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:1234@localhost/lexus'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db=db_connector(app)

from employee_manager.routes.getEmployee import get_employee
from employee_manager.routes.getEmployees import get_employees
from employee_manager.routes.addEmployee import add_employee
from employee_manager.routes.deleteEmployee import delete_employee
from employee_manager.routes.updateEmployee import update_employee
from employee_manager.middleware.validator import validate_details

app.register_blueprint(get_employee)
app.register_blueprint(get_employees)
app.register_blueprint(add_employee)
app.register_blueprint(delete_employee)
app.register_blueprint(update_employee)


