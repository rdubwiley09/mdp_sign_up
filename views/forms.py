from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email, Length
from wtforms_alchemy import PhoneNumberField
from flask_admin.form.widgets import DatePickerWidget
from wtforms.fields.html5 import DateField

class SignUp(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired()], render_kw={"placeholder": "First Name"})
    middle_initial = StringField('Middle Initial', validators=[Length(max=1)], render_kw={"placeholder": "Middle Initial"})
    last_name = StringField('Last Name', validators=[DataRequired()], render_kw={"placeholder": "Last Name"})
    address = StringField('Address', validators=[DataRequired()], render_kw={"placeholder": "Address"})
    city = StringField('City', validators=[DataRequired()], render_kw={"placeholder": "City"})
    zip_code = StringField('Zip Code', validators=[Length(min=5)], render_kw={"placeholder": "Zip"})
    phone_number = PhoneNumberField(validators=[DataRequired()], render_kw={"placeholder": "Phone Number"})
    email = StringField('Email', validators=[Email()], render_kw={"placeholder": "Email"})
    date_of_birth = DateField('Date of Birth', render_kw={"class":"datepicker"})
    gender = StringField('Gender', render_kw={"placeholder": "Gender"})
    registered_to_vote = BooleanField('Registered in Michigan?')
    receive_emails = BooleanField('Recieve Emails?')
    receive_texts = BooleanField('Recieve Texts?')
    submit = SubmitField('Sign Up!')

class EmailForm(FlaskForm):
    email = StringField('Email', validators=[Email(), DataRequired()], render_kw={"placeholder": "Email"})
    submit = SubmitField('Send Email')
