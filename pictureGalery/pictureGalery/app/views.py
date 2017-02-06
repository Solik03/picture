"""
Definition of views.
"""
from django.shortcuts import render, render_to_response
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from django.shortcuts import render
from django import forms
from django.http.response import HttpResponse, HttpResponseRedirect
from app.models import *
import json
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from builtins import print
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as auth_login

def home(request):
	if 'cart' in request.session:
		count = len(request.session['cart'])
	else:
		count = 0;
	html = render(request,'app/tmp/home.html',{'count':count})
	return html

def stile(request):
	html = render(request,'app/tmp/stile/first.html')
	return html


def registration(request):
	if request.method == 'POST':
		name =  request.POST.get('username')
		mail = request.POST.get('email')
		tel = request.POST.get('telephone')
		pas = request.POST.get('password')
		confirmPassword = request.POST.get('confirm-password')
		if pas != confirmPassword:
			return HttpResponse('wrong password')
		bd = CastomUser.objects.create_user(username = name, telephone = tel, email = mail, password = pas)
		bd.save()
		user = authenticate(username = name, password = pas)
		auth_login(request,user)
		return HttpResponseRedirect('/')

@csrf_exempt
def register_ajax(request):
	if request.method == 'POST':
		data = json.loads(request.body.decode('utf-8'))
		name = data['username']
		if CastomUser.objects.filter(username = name):
			return HttpResponse(json.dumps({'free': False}))
		return  HttpResponse(json.dumps({'free': True}))

def login(request):
	name =  request.POST.get('username')
	pas = request.POST.get('password')
	user = authenticate(username = name, password = pas)
	if user is not None:
		auth_login(request,user)	
		return HttpResponseRedirect('/')
	return HttpResponseRedirect('/')

def logout_user(request):
	logout(request)
	return HttpResponseRedirect('/')

def paintings(request):
	picture_list = Picture.objects.all()
	paginator = Paginator(picture_list, 3)
	page = request.GET.get('page')
	try:
		pictures = paginator.page(page)
	except PageNotAnInteger:
        # If page is not an integer, deliver first page.
		pictures = paginator.page(1)
	except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
		pictures = paginator.page(paginator.num_pages)
	if 'cart' in request.session:
		count = len(request.session['cart'])
	else:
		count = 0;
	return render(request,'app/tmp/pictures.html', {"pictures": pictures,'count':count})

@csrf_exempt
def cart_ajax(request):
	data = json.loads(request.body.decode('utf-8'))
	id = int(data['id'])
	if 'cart' not in request.session:
		request.session['cart'] = []
	if id not in request.session['cart']:
		request.session['cart'].append(id)
		request.session.modified = True
	return HttpResponse(json.dumps({'free': True, 'count':len(request.session['cart'])}))


def cart(request):
	if 'cart' not in request.session or not request.session['cart']:
		return HttpResponseRedirect('/')
	pic=request.session['cart']
	pictures = []
	for e in pic:
		pictures.append(Picture.objects.get(id=e))
	sum_cost = sum(p.cost for p in pictures)
	return render(request,'app/tmp/cart.html', {"pictures": pictures, "sum": sum_cost})

@csrf_exempt
def cart_del(request):
	data = json.loads(request.body.decode('utf-8'))
	id = int(data['id'])
	request.session['cart'].remove(id)
	request.session.modified = True
	return HttpResponse(json.dumps({'free': True}))

def save_cart(request):
	pic = request.session['cart']
	client = request.user.username
	pictures = []
	for e in pic:
		bd = Card(customer = CastomUser.objects.get_by_natural_key(client),product = Picture.objects.get(id=e))
		bd.save()
		pic.remove(e)
		request.session.modified = True
	return HttpResponse("Thank you for your purchase")
@csrf_exempt
def message(request):
	if request.method == 'POST':
		name =  request.POST.get('name')
		mail = request.POST.get('email')
		comment = request.POST.get('comments')
		bd = Messages(name=name,email = mail, massage = comment)
		bd.save()
		return HttpResponse("Thank you for your message")
	return HttpResponse("Message not correct!")



