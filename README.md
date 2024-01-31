## Flask Application Design: Manage Emails and Tasks

### Problem Statement:
Develop a Flask web application that provides a user interface to manage emails and tasks effectively, allowing users to compose, send, and receive emails, as well as create, update, and track tasks.

### HTML Files:

1. **index.html**:
   - Serves as the landing page of the application.
   - Contains links to various functionalities of the application (compose email, list emails, tasks, etc.).


2. **compose_email.html**:
   - Provides a form for users to compose and send an email.
   - Includes fields for recipient, subject, and message body.


3. **list_emails.html**:
   - Displays a list of received emails.
   - Each email is represented by sender, subject, and timestamp.
   - Provides actions for reading, replying to, and deleting emails.


4. **tasks.html**:
   - A dynamic page that displays all active tasks.
   - Includes options for creating, editing, and completing tasks.
   - Tasks are organized by priority and due date.


### Routes:

1. **index_page.route**:
   - Endpoint for the index page of the application.
   - Renders the index.html file.


2. **compose_email.route**:
   - Handles the display of the email composition form.
   - Renders the compose_email.html file.


3. **send_email.route**:
   - Processes the email composition form submission.
   - Sends the email using an appropriate library or service.
   - Redirects to list_emails.html.


4. **list_emails.route**:
   - Retrieves all emails from the server / database.
   - Renders the list_emails.html file with the list of emails.


5. **tasks.route**:
   - Retrieves all active tasks from the server / database.
   - Renders the tasks.html file with the list of tasks.


6. **create_task.route**:
   - Processes the task creation form submission.
   - Saves the task in the server / database.
   - Redirects to tasks.html.


7. **edit_task.route**:
   - Handles the display of the task editing form.
   - Populates the form with the details of the task being edited.
   - Renders the editing form.

8. **update_task.route**:
   - Processes the task editing form submission.
   - Updates the task in the server / database.
   - Redirects to tasks.html.


9. **delete_email.route**:
   - Handles the deletion of an email.
   - Deletes the email from the server / database.
   - Redirects to list_emails.html.


10. **complete_task.route**:
    - Handles the completion of a task.
    - Marks the task as completed in the server / database.
    - Redirects to tasks.html.