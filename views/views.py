from flask import Flask, request, render_template, redirect, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from views.forms import SignUp, EmailForm
from flask_bootstrap import Bootstrap
from datetime import datetime
from sqlalchemy_utils import PhoneNumberType
from views.send_email import sendEmail, message, fail_message, successMessage, not_dropped_off
from ast import literal_eval
from dateutil.relativedelta import relativedelta

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
        return "{'first_name': '%s', 'last_name': '%s', 'email': '%s', 'drop_off_time': '%s'}" %(self.first_name, self.last_name, self.email, self.drop_off_time)

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
        subj = "Thank you for signing up!"
        sendEmail(signup.email.data, signup.first_name.data, subj, message, False)
        return redirect(url_for('finish'))
    else:
        if request.method == "POST":
            flash("If not on Chrome: try entering date of birth as: yyyy-mm-dd")
    return render_template('/index.jade', response=signup, title = "Sign-up for the MDP in 30 seconds")

@app.route("/finish", methods=['GET', 'POST'])
def finish():
    return render_template('/finish.jade')

@app.route("/about")
def about():
    return render_template("/about.jade")

@app.route("/membership", methods=['GET', 'POST'])
def sendMessage():
    emform = EmailForm()
    if emform.validate_on_submit():
        records = literal_eval(str(SignUpRecord.query.filter_by(email=emform.email.data).all()))
        if records:
            data = []
            for item in records:
                if item['drop_off_time'] != "None":
                    data.append(item)
            try:
                record = data[-1]
                expiration = datetime.strptime(record['drop_off_time'].split(" ")[0], '%Y-%m-%d') + relativedelta(years=1)
                sendEmail(emform.email.data, record['first_name'], "Membership Verification", successMessage(record['first_name'], record['last_name'], str(expiration.strftime('%m-%d-%Y'))), False)
            except Exception as e:
                record = records[-1]
                sendEmail(emform.email.data, record['first_name'], "Membership Verfication", not_dropped_off, False)
        else:
            sendEmail(emform.email.data, "Recipient", "Membership Verification (Failure)", fail_message, False)
        flash("Email Sent!")
    return render_template('/membership.jade', response=emform, title = "Check Your MDP Registration Status")
