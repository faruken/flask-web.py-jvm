# -*- coding: utf-8 -*-

from functools import wraps
from flask import redirect, url_for
from org.apache.shiro import SecurityUtils
from org.apache.shiro.config import IniSecurityManagerFactory


def singleton(cls):
  # pep318
  _instance = {}
  def getinstance():
    if cls not in _instance:
      _instance[cls] = cls()
    return _instance[cls]
  return getinstance


@singleton
def _subject():
  factory = IniSecurityManagerFactory("classpath:shiro.ini")
  securityManager = factory.getInstance()
  SecurityUtils.setSecurityManager(securityManager)
  return SecurityUtils.getSubject()


def login_required(func):
  @wraps(func)
  def wrapper(r, *args, **kwargs):
    user = _subject()
    if not user.isAuthenticated():
      return redirect(url_for('index'))
    return func(r, *args, **kwargs)
  return wrapper
