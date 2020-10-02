from employee_manager import db

employee_dept=  db.Table('employee_dept',
                db.Column('eid',db.Integer,db.ForeignKey('Employees.eid'),primary_key=True),
                db.Column('dept_id',db.Integer,db.ForeignKey('Departments.dept_id'),primary_key=True)
                 )



class Employee(db.Model):
    __tablename__='Employees'
    eid=db.Column(db.Integer,primary_key=True)
    firstname=db.Column(db.String,nullable=False)
    lastname=db.Column(db.String,nullable=False)
    email=db.Column(db.String,nullable=False)
    mobile_no=db.Column(db.String,nullable=False)
    doj=db.Column(db.Date,nullable=False)
    departments=db.relationship('Department',secondary=employee_dept,backref=db.backref('employees',lazy=True))
    

    def __init__(self,firstname,lastname,email,mobile_no,doj):
        self.firstname=firstname
        self.lastname=lastname
        self.email=email
        self.mobile_no=mobile_no
        self.doj=doj

dept_proj=db.Table( 'dept_proj',
                     db.Column('dept_id',db.Integer,db.ForeignKey('Departments.dept_id'),primary_key=True),
                     db.Column('pid',db.Integer,db.ForeignKey('Projects.pid'),primary_key=True)
                   )

class Department(db.Model):
    __tablename__='Departments'
    dept_id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String,nullable=False)
    projects=db.relationship('Project',secondary=dept_proj,backref=db.backref('departments',lazy=True))

    def __init__(self,name):
        self.name=name

class Project(db.Model):
    __tablename__='Projects'
    pid=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.Integer,unique=True,nullable=False)
    
    def __init__(self,name):
        self.name=name

         