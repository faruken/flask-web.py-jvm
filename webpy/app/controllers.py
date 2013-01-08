# -*- coding: utf-8 -*-

from org.apache.shiro.crypto.hash import Sha256Hash
from org.apache.shiro.authc import AuthenticationException, UsernamePasswordToken, IncorrectCredentialsException
from org.slf4j import Logger, LoggerFactory

import web
from app.forms import LoginForm
from app.decorators import singleton, _subject, login_required

render = web.template.render('app/views')
SALT_KEY = "jBseZIr15E9V36Ks7BgQT5b8pXxqgABVhcNivsrendNkI13"


class IndexHandler(object):

  def sanitize(self, val):
    val = val.strip()
    return web.net.websafe(val)

  def do_login(self, username, password):
    username = self.sanitize(username)
    password = Sha256Hash(password, SALT_KEY, 2048).toBase64()
    user = _subject()
    session = user.getSession()
    if not user.isAuthenticated():
      token = UsernamePasswordToken(username, password)
      token.setRememberMe(True) # By default, Shiro's session expire is 30 min.
      try:
        user.login(token)
      except IncorrectCredentialsException, e:
        return False
    return True

  def GET(self):
    web.header('Content-Type', 'text/html; charset=UTF-8')
    form = LoginForm()
    return render.index(form)

  def POST(self):
    web.header('Content-Type', 'text/html; charset=UTF-8')
    form = LoginForm(None, web.input())
    if form.validate():
      flag = self.do_login(form.username.data, form.password.data)
      if not flag:
        return render.index(form)
      raise web.seeother('/done?true')
    return render.index(form)


class LoginHandler(object):
  @login_required
  def GET(self):
    web.header('Content-Type', 'text/html; charset=UTF-8')
    user = _subject()
    return render.login(user)


class LogoutHandler(object):
  def GET(self):
    _subject().logout()
    raise web.seeother(web.ctx.homedomain)
