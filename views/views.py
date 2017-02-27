from flask import Flask, request, render_template, redirect, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from views.forms import SignUp
from flask_bootstrap import Bootstrap
from datetime import datetime
from sqlalchemy_utils import PhoneNumberType

app  = Flask(__name__)
app.config.from_object('config')
#app.config.from_pyfile('config.py')
db = SQLAlchemy(app)
app.jinja_env.add_extension('pyjade.ext.jinja.PyJadeExtension')
Bootstrap(app)

class SignUpRecord(db.Model):
    __tablename__ = 'sign_up'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.Text)
    middle_initial = db.Column(db.Text)
    last_name = db.Column(db.Text)
    address = db.Column(db.Text)
    city = db.Column(db.Text)
    zip_code = db.Column(db.Text)
    phone_number = db.Column(PhoneNumberType())
    email = db.Column(db.String(100))
    date_of_birth = db.Column(db.Date)
    gender = db.Column(db.Text)
    registered_to_vote = db.Column(db.Boolean)
    receive_emails = db.Column(db.Boolean)
    receive_texts = db.Column(db.Boolean)
    sign_up_time = db.Column(db.DateTime)
    email_time = db.Column(db.DateTime)
    drop_off_time = db.Column(db.DateTime)

    def __init__(self, first_name, middle_initial, last_name, address, city, zip_code, phone_number, email, date_of_birth, gender, registered_to_vote, receive_emails, receive_texts, sign_up_time, email_time, drop_off_time):
        self.first_name = first_name
        self.middle_initial = middle_initial
        self.last_name = last_name
        self.address = address
        self.city = city
        self.zip_code = zip_code
        self.phone_number = phone_number
        self.email = email
        self.date_of_birth = date_of_birth
        self.gender = gender
        self.registered_to_vote = registered_to_vote
        self.receive_emails = receive_emails
        self.receive_texts = receive_texts
        self.sign_up_time = sign_up_time
        self.email_time = email_time
        self.drop_off_time = drop_off_time

    def __repr__(self):
        return "{'first_name': '%s', 'last_name': '%s', 'email': '%s'}" %(self.first_name, self.last_name, self.email)

@app.route("/", methods=['GET', 'POST'])
def signup():
    signup = SignUp(csrf_enable=False)
    form_data = session.get('form_data')
    if signup.validate_on_submit():
        time = datetime.now()
        new_sign_up = SignUpRecord(signup.first_name.data,
                                   signup.middle_initial.data,
                                   signup.last_name.data,
                                   signup.address.data,
                                   signup.city.data,
                                   signup.zip_code.data,
                                   signup.phone_number.data,
                                   signup.email.data,
                                   signup.date_of_birth.data,
                                   signup.gender.data,
                                   signup.registered_to_vote.data,
                                   signup.receive_emails.data,
                                   signup.receive_texts.data,
                                   time,
                                   None,
                                   None)
        db.session.add(new_sign_up)
        db.session.commit()
        return redirect(url_for('finish'))
    return render_template('/index.jade', response=signup, title = "Michigan for Revolution Sign-up")

@app.route("/finish", methods=['GET', 'POST'])
def finish():
    return render_template('/finish.jade')
