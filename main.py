
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(80))
    time_slot = db.Column(db.String(80))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/planner', methods=['POST'])
def planner():
    task = request.form['task']
    time_slot = request.form['time_slot']
    new_task = Task(task=task, time_slot=time_slot)
    db.session.add(new_task)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/static')
def serve_static():
    return render_template('static.html')

if __name__ == '__main__':
    app.run(debug=True)
