from employee_manager import db

class Employee(db.Model):
    __tablename__='Employees'
    eid=db.Column(db.Integer,primary_key=True)
    firstname=db.Column(db.String,nullable=False)
    lastname=db.Column(db.String,nullable=False)
    department=db.Column(db.String,nullable=False)
    email=db.Column(db.String,nullable=False)
    mobile_no=db.Column(db.String,nullable=False)
    doj=db.Column(db.Date,nullable=False)

    def __init__(self,firstname,lastname,department,email,mobile_no,doj):
        self.firstname=firstname
        self.lastname=lastname
        self.department=department
        self.email=email
        self.mobile_no=mobile_no
        self.doj=doj
