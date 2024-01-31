
# Import required modules
from flask import Flask, render_template, request, redirect, url_for
import sqlite3

# Initialize the Flask app
app = Flask(__name__)

# Database Configuration
conn = sqlite3.connect('email_task_manager.db')
c = conn.cursor()

# Index Page
@app.route('/')
def index_page():
    return render_template('index.html')


# Compose Email
@app.route('/compose_email')
def compose_email():
    return render_template('compose_email.html')


# Send Email
@app.route('/send_email', methods=['POST'])
def send_email():
    recipient = request.form['recipient']
    subject = request.form['subject']
    message = request.form['message']
    
    # Send the email using an appropriate library or service
    
    return redirect(url_for('list_emails'))


# List Emails
@app.route('/list_emails')
def list_emails():
    # Fetch emails from the database
    emails = c.execute("SELECT * FROM emails").fetchall()
    
    return render_template('list_emails.html', emails=emails)


# Tasks Page
@app.route('/tasks')
def tasks():
    # Fetch active tasks from the database
    tasks = c.execute("SELECT * FROM tasks WHERE completed=0").fetchall()
    
    return render_template('tasks.html', tasks=tasks)


# Create Task
@app.route('/create_task', methods=['POST'])
def create_task():
    title = request.form['title']
    description = request.form['description']
    priority = request.form['priority']
    due_date = request.form['due_date']
    
    # Insert the task into the database
    c.execute("INSERT INTO tasks (title, description, priority, due_date) VALUES (?, ?, ?, ?)",
              (title, description, priority, due_date))
    conn.commit()
    
    return redirect(url_for('tasks'))


# Edit Task
@app.route('/edit_task/<int:task_id>')
def edit_task(task_id):
    # Fetch the task details from the database
    task = c.execute("SELECT * FROM tasks WHERE id=?", (task_id,)).fetchone()
    
    return render_template('edit_task.html', task=task)


# Update Task
@app.route('/update_task/<int:task_id>', methods=['POST'])
def update_task(task_id):
    title = request.form['title']
    description = request.form['description']
    priority = request.form['priority']
    due_date = request.form['due_date']
    
    # Update the task in the database
    c.execute("""
        UPDATE tasks 
        SET title=?, description=?, priority=?, due_date=?
        WHERE id=?
    """, (title, description, priority, due_date, task_id))
    conn.commit()
    
    return redirect(url_for('tasks'))


# Delete Email
@app.route('/delete_email/<int:email_id>')
def delete_email(email_id):
    # Delete the email from the database
    c.execute("DELETE FROM emails WHERE id=?", (email_id,))
    conn.commit()
    
    return redirect(url_for('list_emails'))


# Complete Task
@app.route('/complete_task/<int:task_id>')
def complete_task(task_id):
    # Mark the task as completed in the database
    c.execute("UPDATE tasks SET completed=1 WHERE id=?", (task_id,))
    conn.commit()
    
    return redirect(url_for('tasks'))


# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
