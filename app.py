# importing necessary libraries and functions
from flask import Flask, jsonify, request, url_for, flash, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

import json

# first step in starting a flask app
app = Flask(__name__)

# configuring the database
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

# initializing sqlalchemy
db = SQLAlchemy(app)


class Database(db.Model,CustomSerializerMixin):
    id= db.Column(db.Integer(), primary_key=True)
    school = db.Column(db.String(1000),)
    department = db.Column(db.String(1000))
    level = db.Column(db.Integer)


# @app.route('/', methods = ['GET', 'POST'])
# def home():
#     info = Database.query.all()

    


@app.route('/', methods=[ 'POST', 'GET'])
def add():
    if request.method == 'POST':
        school = request.form.get('school')
        department = request.form.get('department')
        level = request.form.get('level')
        if school != '' and department != '' and level != '':
                queryset = Database(school=school, department=department, level=level)
                db.session.add(queryset)
                db.session.commit()
                info = Database.query.all()
                info = {
                        "data" : Database(school=school, department=department, level=level),
                    }
  
                return jsonify(info=info) 
        else:
            flash('pls input data in the required fields', 'warning')
            return render_template ('home.html')
    return render_template ('home.html')

 
  
# driver function
if __name__ == '__main__':
    app.secret_key = "code"
    app.run(debug = True)