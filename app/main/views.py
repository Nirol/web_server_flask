from datetime import datetime
from flask import render_template, session, redirect, url_for, abort, flash
from flask_login import login_required, current_user

from app import db
from decorators import permission_required, admin_required
from models import Permission, User
from . import main
from .forms import  EditProfileForm


@main.route('/', methods=['GET', 'POST'])
def index():
    return "lol123"
    # return render_template('index.html',
    #                        name=session.get('name'),
    #                        known=session.get('known', False),
    #                        current_time=datetime.utcnow())


@main.route('/admin')
@login_required
@admin_required
def for_admins_only():
    return "For administrators!"


@main.route('/moderator')
@login_required
@permission_required(Permission.MODERATE_COMMENTS)
def for_moderators_only():
    return "For comment moderators!"


@main.route('/secret')
@login_required
def secret():
    return 'Only authenticated users are allowed!'


@main.route('/user/<username>')
def user(username):
    user = User.query.filter_by(username=username).first()
    if user is None:
        abort(404)
        return render_template('user.html', user=user)


@main.route('/edit-profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = EditProfileForm()
    if form.validate_on_submit():
        current_user.name = form.name.data
        current_user.location = form.location.data
        current_user.about_me = form.about_me.data
        db.session.add(user)
        flash('Your profile has been updated.')
        return redirect(url_for('.user', username=current_user.username))
    form.name.data = current_user.name
    form.location.data = current_user.location
    form.about_me.data = current_user.about_me
    return render_template('edit_profile.html', form=form)
