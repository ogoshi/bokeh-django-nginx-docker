#!/usr/bin python3.6
#Itamar Almeida
# -*- coding: utf-8 -*-

import time
from django.contrib.auth.decorators import login_required

from pprint import pprint

from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.http import JsonResponse
from django.urls import reverse

from .dashboard import LayoutDashBoard

import json
import numpy.ma as ma

from bokeh.embed import server_document, components

from .dashboard import LayoutDashBoard

step = 0

import numpy as np

from .utils import port


def index(request):
	plots = []

	script = server_document('http://127.0.0.1:{}/gmap'.format(port))
	pprint(script)
	return render(request, 'site/index.html', {'script':script})

@csrf_exempt
def dashboard(request):

        return JsonResponse({'itamar':"itamar"})


