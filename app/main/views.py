# -*- coding: utf-8 -*-

from os import abort
from flask import redirect, url_for, render_template
from flask_login import current_user
from . import main
from app.models import User


@main.route('/', methods=['GET', 'POST'])
def index():
    if current_user.is_authenticated():
        return render_template('index.html')
    else:
        return redirect(url_for('auth.login'))


@main.route('/user/<username>')
def user(username):
    present_user = User.query.filter_by(name=username).first()
    if present_user is None:
        abort(404)
    return render_template('user.html', user=present_user)