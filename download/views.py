from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .tasks import zip_maker
import requests
from paymeuz.models import Transaction
from cart.models import *
from .tasks import send_download_page
from cart.models import OrderSingleItem
from urllib3 import get_host
from django.db.models import F
from product.models import Product


def create_verify(request, number, exp_date, amount):
	# url = "http://www.3d-models.uz" + request.path[:3] + "/api/payme/card/create/"
	uri = request.build_absolute_uri().split('/')
	domain = uri[0]+'//'+uri[2]+'/'+uri[3]+'/'
	
	url = domain + "api/payme/card/create/"
	data = dict(
		id = id,
		params = dict(
			card = dict(
				number = number,
				expire = exp_date,
			),
			amount = amount,
			save = True
		)
	)
	try:
	    response = requests.post(url, json = data)
	    result = response.json()
	    return result
	except:
	    return {}


try:
	id = Transaction.objects.all().count() + 1
except:
	pass
amount = 0

# @login_required
def card_verify_code(request):
	if request.method == 'POST':
		uri = request.build_absolute_uri().split('/')
		domain = uri[0]+'//'+uri[2]+'/'+uri[3]+'/'
		# url1   = 'http://www.3d-models.uz' + request.path[:3] + '/api/payme/card/verify/'
		url1   = domain + 'api/payme/card/verify/'
		token  = request.POST['token']
		code   = request.POST['verify_code']
		price  = request.POST['amount']
		modelid = request.POST['blogid']
		print(type(modelid), modelid)

		amount = float(price) * 100
		print("amount: ", type(amount))
		data1 = dict(
			id     = id,
			params = dict(
				token = token,
				code  = code,
			)
		)
		r = requests.post(url1, json=data1)
		result = r.json()

		# url2  = 'http://www.3d-models.uz' + request.path[:3] + '/api/payme/payment/'
		
		url2  = domain + 'api/payme/payment/'
		data2 = dict(
			id     = id,
			params = dict(
				token   = token,
				amount  = amount,
				account = dict(
					order_id = id
				)
			)
		)
		rq = requests.post(url2, json=data2)
		rs = rq.json()

		try:
			if rs['result']['receipt']['error'] == None:
				print("successfully")
				customer = request.user.customer
				if modelid != 'None':
					send_download_page(request, customer, modelid)
				else:
					send_download_page(request, customer)
			else:
				print("Houston, we have a problem! :(")
		except Exception as e:
			print("Houston, we have a problem! :(\n", e)
		return redirect('Core:go_to_email')
	return render(request, "card_verify.html")


from . import tasks
def tokenize_address(request, token):
	token = ''
	return redirect(tasks.link)


from django.http import HttpResponse
try:
	from StringIO import StringIO
except ImportError:
	from io import StringIO, BytesIO
from zipfile import ZipFile
import os
from django.conf import settings
from cart.models import Customer

def make_models_zip(request, pk, os_pk=None, *args, **kwargs):

	# if request.user.is_authenticated:
	# 	customer = request.user.customer
	# 	order, created = Order.objects.get_or_create(customer=customer, complete=False)
	# 	print("Order: ", order, '\n', "Created: ", created)
	# 	items = order.orderitem_set.all()
	model_locations = []
	customer = Customer.objects.get(pk=pk)

	if os_pk:
		order = OrderSingleItem.objects.get(pk=os_pk)
		model_locations.append(order.model.model_file.path)
		Product.objects.filter(slug=order.model.slug).update(downloaded=F('downloaded') + 1)
		return  zip_maker(model_locations, customer)
	else:
		order = Order.objects.get(customer=customer, complete=False)
		items = order.orderitem_set.all()
		
		if len(items) > 0:
			for model in  items:
				if model.cart_field:
					model_locations.append(model.model.model_file.path)
					Product.objects.filter(slug=model.model.slug).update(downloaded=F('downloaded') + 1)
			return  zip_maker(model_locations, customer)
	return
