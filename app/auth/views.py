# -*- coding: utf-8 -*-

from flask import render_template
from . import auth

@auth.route('/login')
def login():
    login = LoginForm()
    if form.validate_on_submit():
        pass
    return render_template('auth/login.html')
