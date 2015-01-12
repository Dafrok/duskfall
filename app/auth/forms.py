# -*- coding: utf-8 -*-

from flask.ext.wtf import Form
from wtforms import StringFiled, PasswordField, BooleanField, SubmitField
from wtforms.validators import Required, Email


class LoginForm(Form):
    email = StringField('Email', validators=[Required(), length(1, 64),
                                             Email()])

    password = PasswordField('Password', validators=[Required()])
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField('log In')