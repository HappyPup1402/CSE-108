from flask import Flask, render_template, request, jsonify
import json
app = Flask(__name__)

@app.route("/")
@app.route("/gradeinfo")
def gradeInfo():
    return render_template('gradesInfo.html')

@app.route('/grades', methods = ['GET'])
def getGrades():
    grades = json.load(open('grades.json'))
    return grades

@app.route('/grades/<id>', methods = ['GET'])
def getStudent(id):
    grades = json.load(open('grades.json'))
    if id in grades:
        return {id: grades[id]}

@app.route('/grades' , methods = ['POST'])
def addStudent():
    submission = request.get_json()
    grades = json.load(open('grades.json'))
    grades[submission['name']] = submission['grade']
    jsonFile = open("grades.json", "w")
    json.dump(grades, jsonFile)
    jsonFile.close()
    return grades

@app.route('/grades/<id>', methods = ['PUT'])
def editGrade(id):
    grades = json.load(open('grades.json'))
    if id in grades:
        submission = request.get_json()
        grades[id] = submission['grade']
        jsonFile = open("grades.json", "w")
        json.dump(grades, jsonFile)
        jsonFile.close()
        return grades

@app.route('/grades/<id>', methods = ['DELETE'])
def deleteStudent(id):
    grades = json.load(open('grades.json'))
    if id in grades:
        del grades[id]
        jsonFile = open("grades.json", "w")
        json.dump(grades, jsonFile)
        jsonFile.close()
        return grades

if __name__ == "__main__":
    app.run()