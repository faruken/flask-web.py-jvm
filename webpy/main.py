#!/usr/bin/env python
# -*- coding: utf-8 -*-

import web
from urls import URLS

web.config.debug = True
app = web.application(URLS, globals(), autoreload=False)

if __name__ == '__main__':
  app.run()
