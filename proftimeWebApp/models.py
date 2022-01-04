from proftimeWebApp import db

class User(db.Model):
    
    id = db.Column(db.Integer, primary_key =True)
    username= db.Column (db.String(20), unique = True, nullable = False)
    email= db.Column (db.String(120), unique = True, nullable = False)
    password= db.Column (db.String(60), nullable = False)
    
    def __repr__(self):
        return f"User('{self.username}', '{self.email}',)"
    
class Faculty(db.Model):
    
    id = db.Column(db.Integer, primary_key = True)
    facultyname= db.Column (db.String(120), nullable = False)
    designation= db.Column (db.String(120), nullable = False)
    officelocation= db.Column (db.String(160), nullable = False)
    contactinfo= db.Column (db.String(160), nullable = False)
    days= db.Column (db.String(120), nullable = False)
    times= db.Column (db.String(160), nullable = False)
    
    def __repr__(self):
        return f"User('{self.facultyname}', '{self.designation}',)"
    