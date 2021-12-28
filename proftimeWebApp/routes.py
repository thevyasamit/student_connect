from flask import *
from proftimeWebApp import  app, db, bcrypt
from proftimeWebApp.models import User

@app.route("/login", methods =['GET','POST'])
def login():
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        # Create variables for easy access
        user = User.query.filter_by(email = request.form['username']).first() #username is same as email in the form(login.html) so pleae change that confusion in future if possible
        if (user.email == request.form['username']) and (bcrypt.check_password_hash(user.password, request.form['password'])):
            return render_template('/profile.html', msg = user.username) 
        else:
            return render_template('/profile.html', msg = "Wrong Passsword !!!")  
    else:
        return render_template('/login.html')

@app.route("/signup", methods = ['GET','POST'])
def signup():
    if request.method == 'POST' and 'username' in request.form and 'email' in request.form and 'password' in request.form:
        password = request.form['password']
        hashPassword = bcrypt.generate_password_hash(request.form['password']).decode('utf-8')
        
        user = User(username = request.form['username'], email = request.form['email'], password = hashPassword)
        db.session.add(user)
        db.session.commit()
        
        return render_template("/login.html", msg = "User successfully Created!!! now please login")
    else:
        return render_template("/signup.html", msg = "User NOT Created XXXX")
        
        
    
@app.route("/")
def main():
    return render_template("/signup.html")