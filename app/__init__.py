from flask import Flask
from flask_mail import Mail


app = Flask(__name__)
app.config['SECRET_KEY'] = 'enter some random passphrase'
app.config['MAIL_SERVER'] = 'smtp.mailtrap.io'
app.config['MAIL_PORT'] = '2525' 
app.config['MAIL_USERNAME'] = 'f5dab85f6a961b'
app.config['MAIL_PASSWORD'] = '212875bf55a172'

mail = Mail(app)
from app import views