# -*- coding: utf-8 -*-

from wtforms import Form, TextField, PasswordField, validators

class LoginForm(Form):
  username = TextField("username", validators=[validators.required("Please write your username.")])
  password = PasswordField("password", validators=[validators.required("Please write your password.")])
