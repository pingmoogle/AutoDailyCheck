# -*- encoding: UTF-8 -*-

# config.py
import os
import multiprocessing
import gevent
from gevent import monkey

gevent.monkey.patch_all()

# debug = True
loglevel = 'debug'
bind = "0.0.0.0:8099"
pidfile = "log/gunicorn.pid"
accesslog = "log/access.log"
errorlog = "log/debug.log"
daemon = True

workers = multiprocessing.cpu_count()*2+1
worker_class = 'gevent'
x_forwarded_for_header = 'X-FORWARDED-FOR'
