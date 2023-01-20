from proftimeWebApp import app,db
if __name__ == '__main__':
    db.create_all()
    # Adding host = 0.0.0.0 is used so that it can be used with docker.
    app.run(host='0.0.0.0',debug = True)