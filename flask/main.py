# -*- coding: utf-8 -*-

from flask import Flask, render_template, request, redirect, url_for
from flask.views import MethodView
from forms import LoginForm
from decorators import login_required, _subject

from org.apache.shiro.crypto.hash import Sha256Hash
from org.apache.shiro.authc import AuthenticationException, UsernamePasswordToken, IncorrectCredentialsException
from org.slf4j import Logger, LoggerFactory

SALT_KEY = "jBseZIr15E9V36Ks7BgQT5b8pXxqgABVhcNivsrendNkI13"

app = Flask(__name__)
app.config.from_object(__name__)

class IndexHandler(MethodView):
  
  def do_login(self, username, password):
    password = Sha256Hash(password, SALT_KEY, 2048).toBase64()
    print password
    user = _subject()
    session = user.getSession()
    if not user.isAuthenticated():
      token = UsernamePasswordToken(username, password)
      token.setRememberMe(True)
      try:
        user.login(token)
      except IncorrectCredentialsException, e:
        return False
    return True
  
  def get(self):
    form = LoginForm(request.form)
    return render_template('index.html', form=form)
  
  def post(self):
    form = LoginForm(request.form)
    if form.validate():
      flag = self.do_login(form.username.data, form.password.data)
      print flag
      if not flag:
        return render_template('index.html', form=form)
      return redirect(url_for('login'))
    else:
      return render_template('index.html', form=form)


class LoginHandler(MethodView):
  @login_required
  def get(self):
    user = _subject()
    return render_template('login.html', currentUser=user)


class LogoutHandler(MethodView):
  def get(self):
    _subject().logout()
    return redirect(url_for('index'))


app.add_url_rule('/', view_func=IndexHandler.as_view('index'))
app.add_url_rule('/login', view_func=LoginHandler.as_view('login'))
app.add_url_rule('/logout', view_func=LogoutHandler.as_view('logout'))


if __name__ == '__main__':
  app.run(debug=True)
