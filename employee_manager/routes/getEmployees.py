from flask import jsonify,Blueprint


get_employees=Blueprint('get_employees',__name__)

@get_employees.route('/getEmployees',methods=['GET'])
def get():
    return jsonify({'msg':'getEmployees'})