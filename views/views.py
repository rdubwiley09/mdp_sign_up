from flask import Flask, request, render_template, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from views.forms import SignUp
from flask_bootstrap import Bootstrap
from models.models import x
from flask_wtf.csrf import CSRFProtect

app  = Flask(__name__)
app.config.from_object('config')
app.config.from_pyfile('config.py')
app.jinja_env.add_extension('pyjade.ext.jinja.PyJadeExtension')
Bootstrap(app)

@app.route("/", methods=['GET', 'POST'])
def main():
    response = SignUp(meta.csrf=False)
    if response.validate_on_submit():
        redirect(success)
    return render_template('/index.jade', response=response)


@app.route('/success')
def success():
    return('good job!')

'''sign = User(form.first_name,
            form.last_name,
            form.phone_number,
            form.email,
            form.address,
            form.city,
            form.zip_code,
            form.receive_emails,
            form.receive_texts)'''
