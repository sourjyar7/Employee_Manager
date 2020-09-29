from flask_sqlalchemy import SQLAlchemy 

def db_connector(app):
    db = SQLAlchemy(app)
    return db

