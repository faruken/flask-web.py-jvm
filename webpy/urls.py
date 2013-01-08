# -*- coding: utf-8 -*-

from app.controllers import IndexHandler, LoginHandler, LogoutHandler


URLS = (
  r'^/done$', LoginHandler,
  r'^/logout$', LogoutHandler,
  r'^/', IndexHandler
)
