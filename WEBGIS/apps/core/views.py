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

import json


from bokeh.embed import server_document, components
from bokeh.client import pull_session


step = 0

from .utils import port


def index(request):
	
	script = server_document(url='http://localhost:5006/gmap')
	
	return render(request, 'site/index.html', {'script':script})

@csrf_exempt
def dashboard(request):

        return JsonResponse({'itamar':"itamar"})
