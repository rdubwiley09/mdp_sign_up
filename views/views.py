from flask import Flask, request, render_template, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from views.forms import SignUp, SignIn
from flask_bootstrap import Bootstrap
from datetime import datetime
from sqlalchemy_utils import PhoneNumberType

app  = Flask(__name__)
app.config.from_object('config')
app.config.from_pyfile('config.py')
db = SQLAlchemy(app)
app.jinja_env.add_extension('pyjade.ext.jinja.PyJadeExtension')
Bootstrap(app)

class SignInRecord(db.Model):
    __tablename__ = 'MI4RevSignIn'
    id = db.Column(db.Integer, primary_key=True)
    event = db.Column(db.Text)
    first_name = db.Column(db.Text)
    last_name = db.Column(db.Text)
    phone_number = db.Column(PhoneNumberType())
    email = db.Column(db.String(100))
    sign_in_time = db.Column(db.DateTime)

    def __init__(self, event, first_name, last_name, phone_number, email, sign_in_time):
        self.event = event
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.email = email
        self.sign_in_time = sign_in_time

class SignUpRecord(db.Model):
    __tablename__ = 'MI4RevSignUp'
    id = db.Column(db.Integer, primary_key=True)
    event = db.Column(db.Text)
    first_name = db.Column(db.Text)
    last_name = db.Column(db.Text)
    phone_number = db.Column(PhoneNumberType())
    email = db.Column(db.String(100))
    address = db.Column(db.Text)
    city = db.Column(db.Text)
    zip_code = db.Column(db.Text)
    receive_emails = db.Column(db.Boolean)
    receive_texts = db.Column(db.Boolean)
    sign_up_time = db.Column(db.DateTime)

    def __init__(self, event, first_name, last_name, phone_number, email, address, city, zip_code, receive_emails, receive_texts, sign_up_time):
        self.event = event
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.email = email
        self.address = address
        self.city = city
        self.zip_code = zip_code
        self.receive_emails = receive_emails
        self.receive_texts = receive_texts
        self.sign_up_time = sign_up_time

@app.route("/signup", methods=['GET', 'POST'])
def signup():
    signup = SignUp(csrf_enable=False)
    event = session.get('event')
    if signup.validate_on_submit():
        session['event'] = signup.event.data
        time = datetime.now()
        new_sign_in = SignUpRecord(signup.event.data,
                                   signup.first_name.data,
                                   signup.last_name.data,
                                   signup.phone_number.data,
                                   signup.email.data,
                                   signup.address.data,
                                   signup.city.data,
                                   signup.zip_code.data,
                                   signup.receive_emails.data,
                                   signup.receive_texts.data,
                                   time)
        db.session.add(new_sign_in)
        db.session.commit()
        redirect('/success')
    return render_template('/index.jade', response=signup, event = event, title = "Michigan for Revolution Sign-up")

@app.route("/signin", methods=['GET', 'POST'])
def signin():
    signin = SignIn()
    event = session.get('event')
    if signin.validate_on_submit():
        time = datetime.now()
        new_sign_in = SignInRecord(signin.event.data,
                                   signin.first_name.data,
                                   signin.last_name.data,
                                   signin.phone_number.data,
                                   signin.email.data,
                                   time)
        db.session.add(new_sign_in)
        db.session.commit()
        session['event'] = signin.event.data
        return redirect(url_for('signup'))
    return render_template('/index.jade', response=signin, event = event, title = "Michigan for Revolution Sign-in")


@app.route('/success')
def success():
    return render_template('/success.jade')
