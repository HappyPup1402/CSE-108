from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)


with app.app_context():
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
    db = SQLAlchemy(app)
    class classroom(db.Model):
        id = db.Column(db.Integer, primary_key = True)
        Name = db.Column(db.String, nullable = False, unique = True)
        Grade = db.Column(db.Float, nullable = False, unique = False)
        def __init__ (self, Name, Grade):
            self.Name = Name
            self.Grade = Grade
    db.create_all()

def myJson(Class):
    json = {}
    for Student in Class:
        json.update({Student.Name:Student.Grade})
    return json

@app.route("/")
@app.route("/gradeinfo")
def gradeInfo():
    return render_template('gradesInfo.html')

@app.route('/grades', methods = ['GET'])
def getGrades():
    return myJson(classroom.query.all()) 

@app.route('/grades/<id>', methods = ['GET'])
def getStudent(id):
    return myJson(classroom.query.filter_by(Name = id))

@app.route('/grades' , methods = ['POST'])
def addStudent():
    submission = request.get_json()
    Name = submission['name']
    Grade = submission['grade'] 
    Student = classroom(Name, Grade)
    db.session.add(Student)
    db.session.commit()
    return myJson(classroom.query.all())

@app.route('/grades/<id>', methods = ['PUT'])
def editGrade(id):
    submission = request.get_json()
    NewGrade = submission['grade']
    Student = classroom.query.filter_by(Name = id)
    Student = Student.update(dict(Grade = NewGrade))
    db.session.commit()
    return myJson(classroom.query.all())

@app.route('/grades/<id>', methods = ['DELETE'])
def deleteStudent(id):
    db.session.delete(classroom.query.filter_by(Name=id).first())
    db.session.commit()
    return myJson(classroom.query.all())

if __name__ == '__main__':
    app.run()