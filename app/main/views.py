# -*- coding: utf-8 -*-

from flask import redirect, url_for
from flask_login import current_user
from . import main

@main.route('/', methods=['GET', 'POST'])
def index():
    if current_user.is_authenticated():
        return redirect('/admin')
    else:
        return redirect(url_for('auth.login'))
