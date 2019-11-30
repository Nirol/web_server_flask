from flask import render_template, session, redirect, url_for, flash
from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import InputRequired
from config import *
import config
from db_models.models import User, Role


class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[InputRequired()])
    submit = SubmitField('Submit')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


@app.route('/', methods=['GET', 'POST'])
def index():
 form = NameForm()
 if form.validate_on_submit():
    old_name = session.get('name')
    if old_name is not None and old_name != form.name.data:
        flash('Looks like you have changed your name!')
    session['name'] = form.name.data
    form.name.data = ''
    return redirect(url_for('index'))
 return render_template('index.html',
    form = form, name = session.get('name'), current_time=datetime.utcnow())



@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)


if __name__ == '__main__':
    from db_models import models

    config.app.run(debug='True')
