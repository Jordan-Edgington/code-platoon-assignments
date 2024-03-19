from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://jordanedgington@localhost/school'

db = SQLAlchemy(app)


class Students_flask(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(10))
    last_name = db.Column(db.String(10))
    age = db.Column(db.Integer)
    grade = db.Column(db.String(1))


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/v1/students/', methods=['GET'])
def get_students():
    students = Students_flask.query.all()
    student_list = [
        {'id': student.id, 'first_name': student.first_name, 'last_name': student.last_name, 'age': student.age, 'grade': student.grade, } for student in students]
    return jsonify(student_list)


@app.route('/api/v1/old_students/', methods=['GET'])
def get_old_students():
    students = Students_flask.query.filter(Students_flask.age > 20).all()
    student_list = [
        {'id': student.id, 'first_name': student.first_name, 'last_name': student.last_name, 'age': student.age, 'grade': student.grade, } for student in students]
    return jsonify(student_list)


@app.route('/api/v1/young_students/', methods=['GET'])
def get_young_students():
    students = Students_flask.query.filter(Students_flask.age < 21).all()
    student_list = [
        {'id': student.id, 'first_name': student.first_name, 'last_name': student.last_name, 'age': student.age, 'grade': student.grade, } for student in students]
    return jsonify(student_list)


@app.route('/api/v1/advance_students/', methods=['GET'])
def get_advance_students():
    students = Students_flask.query.filter(
        Students_flask.age < 21, Students_flask.grade == 'A').all()
    student_list = [
        {'id': student.id, 'first_name': student.first_name, 'last_name': student.last_name, 'age': student.age, 'grade': student.grade, } for student in students]
    return jsonify(student_list)


@app.route('/api/v1/student_names/', methods=['GET'])
def get_student_names():
    students = Students_flask.query.all()
    student_list = [
        {'first_name': student.first_name, 'last_name': student.last_name} for student in students]
    return jsonify(student_list)


@app.route('/api/v1/student_ages/', methods=['GET'])
def get_student_ages():
    students = Students_flask.query.all()
    student_list = [
        {'full_name': f'{student.first_name} {student.last_name}', 'age': student.age} for student in students]
    return jsonify(student_list)


app.run(debug=True, port=8000)
