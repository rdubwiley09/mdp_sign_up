from flask import Flask, request, render_template, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from views.forms import SignUp, SignIn
from flask_bootstrap import Bootstrap
from models.models import x

app  = Flask(__name__)
app.config.from_object('config')
app.config.from_pyfile('config.py')
app.jinja_env.add_extension('pyjade.ext.jinja.PyJadeExtension')
Bootstrap(app)

@app.route("/signup", methods=['GET', 'POST'])
def signup():
    response = SignUp(csrf_enable=False)
    organization = session.get('organization')
    if response.validate_on_submit():
        session['organization'] = response.organization.data
        redirect('/success')
    return render_template('/index.jade', response=response, organization = organization)

@app.route("/signin", methods=['GET', 'POST'])
def signin():
    signin = SignIn()
    organization = session.get('organization')
    if signin.validate_on_submit():
        session['organization'] = signin.organization.data
        return redirect(url_for('signup'))
    return render_template('/index.jade', response=signin, organization = organization)


@app.route('/success')
def success():
    return render_template('/success.jade')

'''sign = User(form.first_name,
            form.last_name,
            form.phone_number,
            form.email,
            form.address,
            form.city,
            form.zip_code,
            form.receive_emails,
            form.receive_texts)'''
