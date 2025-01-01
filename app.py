from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env file

email_address = os.getenv('EMAIL_ADDRESS')
email_password = os.getenv('EMAIL_PASSWORD')

from flask import Flask, render_template, request, redirect
import smtplib

app = Flask(__name__)

# Route to render the homepage (index.html)
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle feedback form submission
@app.route('/submit_feedback', methods=['POST'])
def submit_feedback():
    name = request.form['name']
    email = request.form['email']
    feedback = request.form['feedback']

    # Call a function to send the feedback via email
    send_email(name, email, feedback)

    return redirect('/')  # Redirect back to the homepage after submitting feedback

def send_email(name, email, feedback):
    try:
        # Set up the SMTP server
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()  # Use secure encryption

        # Log in to your Gmail account
        server.login('qtop268@gmail.com', 'qtop@q12Q')

        # Compose the email
        subject = "New Feedback"
        body = f"Name: {name}\nEmail: {email}\nFeedback:\n{feedback}"
        message = f"Subject: {subject}\n\n{body}"

        # Send the email
        server.sendmail('qtop268@gmail.com', 'qtop268@gmail.com', message)

        # Close the connection to the server
        server.quit()

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    app.run(debug=True)
