from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email, Length
from wtforms_alchemy import PhoneNumberField

class SignUp(FlaskForm):
    event = StringField('Event', validators=[DataRequired()], render_kw={"placeholder": "Event"})
    first_name = StringField('First Name', validators=[DataRequired()], render_kw={"placeholder": "First Name"})
    last_name = StringField('Last Name', validators=[DataRequired()], render_kw={"placeholder": "Last Name"})
    phone_number = PhoneNumberField(validators=[DataRequired()], render_kw={"placeholder": "Phone Number"})
    email = StringField('Email', validators=[Email()], render_kw={"placeholder": "Email"})
    address = StringField('Address', validators=[DataRequired()], render_kw={"placeholder": "Address"})
    city = StringField('City', validators=[DataRequired()], render_kw={"placeholder": "City"})
    zip_code = StringField('Zip Code', validators=[Length(min=5)], render_kw={"placeholder": "Zip"})
    receive_emails = BooleanField('Recieve Emails?')
    receive_texts = BooleanField('Recieve Texts?')
    submit = SubmitField('Sign Up!')

class SignIn(FlaskForm):
    event = StringField('Event', validators=[DataRequired()], render_kw={"placeholder": "Event"})
    first_name = StringField('First Name', validators=[DataRequired()], render_kw={"placeholder": "First Name"})
    last_name = StringField('Last Name', validators=[DataRequired()], render_kw={"placeholder": "Last Name"})
    phone_number = PhoneNumberField(validators=[DataRequired()], render_kw={"placeholder": "Phone Number"})
    email = StringField('Email', validators=[Email()], render_kw={"placeholder": "Email"})
    submit = SubmitField('Sign In!')
