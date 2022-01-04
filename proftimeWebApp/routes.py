from flask import *
from proftimeWebApp import  app, db, bcrypt
from proftimeWebApp.models import User, Faculty
from datetime import datetime
import csv

@app.route("/login", methods =['GET','POST'])
def login():
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        user = User.query.filter_by(email = request.form['username']).first() #username is same as email in the form(login.html) so pleae change that confusion in future if possible
        if (user.email == request.form['username']) and (bcrypt.check_password_hash(user.password, request.form['password'])):
            fac = Faculty.query.all()
            facList = []
            for f in fac:
                f = str(f)
                a = f.split(",")[0].split("(")[1].split("'")[1]
                facList.append(a)
            return render_template('/profile.html', usr = user.username, facultyList = facList) 
        else:
            return render_template('/login.html', msg = "Wrong Passsword Please try again !!!")  
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

@app.route("/displayInfo", methods =['GET','POST'])
def displayInfo():
    if request.method == 'POST':
        data3 = ""
        ans = str(request.form['prof'])
        t = ans#.split(",")[0].split("(")[1].split("'")[1]
        data1 = str(Faculty.query.filter_by(facultyname = t).with_entities(Faculty.times).first())
        #data1 = data1.split("(")[1].split("'")[1].split("\n")[0].split("\\")[0]#replace("\n","")#rstrip("\n")
        data2 = str(Faculty.query.filter_by(facultyname = t).with_entities(Faculty.days).first())
        day1 = data2.split("[")[1].split("]")[0].split("'")[1].split("\\")[0]
        day1 = str(day1)
        day2 = data2.split("[")[1].split("]")[0].split("'")[3].split("\\")[0]
        day2 = str(day2)
        dateTime = {"Monday":"Mon",
                    "Tuesday":"Tue",
                    "Wednesday":"Wed",
                    "Thursday": "Thu",
                    "Friday":"Fri",
                    "Saturday":"Sat",
                    "Sunday":"Sun"}
        check = datetime.today().strftime('%A')
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        check = str(check)
        if dateTime[check] == day1:
            data2 = day1
            data1 = data1.split("(")[1].split("'")[1].split("\n")[0].split("\\")[0]
            checkAmPm = int(data1.split(":")[0])
            if data1 == current_time:
                if checkAmPm >= 12:
                    data1 = data1+" pm"
                else:
                    data1 = data1+" am"
                data3 = "AVAILABLE !!"
            else:
                
                if checkAmPm >= 12:
                    data1 = data1+" pm"
                else:
                    data1 = data1+" am"
                
                data3 = "Currently Unavilable!! Next Available " + data1 + " on "+ day2
        elif dateTime[check] == day2:
            data2 = day2
            data1 = data1.split("(")[1].split("'")[1].split("\n")[0].split("\\")[0]
            checkAmPm = int(data1.split(":")[0])
            if data1 == current_time:
                if checkAmPm >= 12:
                    data1 = data1+" pm"
                else:
                    data1 = data1+" am"
                
                data3 = "AVAILABLE !!"
            else:
                if checkAmPm >= 12:
                    data1 = data1+" pm"
                else:
                    data1 = data1+" am"
                
                data3 = "Currently Unavilable!! Next Available " + data1 + " on "+ day1
        else:
            data1 = data1.split("(")[1].split("'")[1].split("\n")[0].split("\\")[0]
            checkAmPm = int(data1.split(":")[0])
            if checkAmPm > 12:
                data1 = data1+" pm"
            else:
                data1 = data1+" am"
            data2 = day1 + " " + day2
            data3 = " NOT AVAILABLE NOW XXX \n"+"Check on "+day1+ " or " + day2

    return render_template('/profile.html', msg1 =data1, msg2 =data2, msg3 =data3)  

# @app.route("/dummydata")
# def dummy():
#     #try:
#     with open("/Users/avyas/Desktop/Projects/github_projects/proftimeWebApp/proftimeWebApp/cseDeptData.csv","r") as csvFile:
#         next(csvFile)
#         for row in csvFile:
#             data = row.split(",")
#             fac = Faculty(facultyname = str(data[0]), designation = str(data[1]), officelocation = str(data[2]), contactinfo= str(data[3]), days = str(data[4]) + str(data[5]) , times= str(data[6]))
#             db.session.add(fac)
#             db.session.commit()
#         #using this to load the csv data to database
#     #except Exception as e:
#         #a = str(type(e))
#     return render_template('/profile.html', msg = 'da') 
#     #else:
#         #return render_template('/profile.html', msg = "DATA ADDED") 
#     #finally:
#     csvFile.close()
    
        
        
    
@app.route("/")
def main():
    return render_template("/signup.html")