 # -*- coding: utf-8 -*-

from bottle import route, run, template, view, static_file
import os.path
import svipul

from multiprocessing import Process

SITE_ROOT = os.path.dirname(os.path.realpath(__file__))

def work():
    svipul.work()

@route('/')
@view('index')
def index():
    return dict()

@route('/work')
def work():
    svipul.work()
    return "done"

@route('/prog')
def work():
    return str(svipul.get_prog())

@route('/static/<filename:path>')
def send_static(filename):
    return static_file(filename, root=os.path.join(SITE_ROOT, 'static'))

run(host='localhost', port=8080, reloader=True, server='cherrypy')