from flask_sqlalchemy import SQLAlchemy

db =SQLAlchemy()

class TaskModel(db.Model):
    __tablename__ = "table"

    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String())
    email = db.Column(db.String())
    priority = db.Column(db.Integer())
    

    def __init__(self, description,email,priority):
        self.description = description
        self.email = email
        self.priority = priority


    def __repr__(self):
        return f"{self.description}:{self.email}:{self.priority}"