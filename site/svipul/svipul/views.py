from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
import svipul
from multiprocessing import Process

progress = 0.0

import threading

class SummingThread(threading.Thread):
     def run(self):
         svipul.work()

def home(request):
    # View code here...
    return render(request, 'index.html', {})


def work(request):
    progress = 0.0
    #svipul.work()
    p = SummingThread()
    p.start()
    p.join()
    return HttpResponse('done')

def prog(request):
    return HttpResponse(str(progress))

def incr_prog():
    global progress
    progress += 1.0


def f(name):
    print 'hello', name
