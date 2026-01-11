from flask import Flask, render_template, request, redirect, url_for
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.simple_db import SimpleDB

app = Flask(__name__)
db = SimpleDB(storage_dir="../data")


db.execute("CREATE TABLE students (id, name, course)")

@app.route('/')
def index():
    rows = db.execute("SELECT * FROM students")
    if isinstance(rows, str): rows = [] 
    return render_template('index.html', students=rows)

@app.route('/add', methods=['POST'])
def add_student():
    id = request.form.get('id')
    name = request.form.get('name')
    course = request.form.get('course')
    
    query = f"INSERT INTO students VALUES ({id}, '{name}', '{course}')"
    db.execute(query)
    
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, port=5000)