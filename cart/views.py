from django.core.paginator import Paginator
from django.db.models import F
from django.core.mail import send_mail
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404, JsonResponse, BadHeaderError
from django.core import serializers
from django.views import View
from django.core.serializers.json import DjangoJSONEncoder
from django.contrib.auth.mixins import LoginRequiredMixin
from django.template import defaultfilters
from django.conf import settings
from django.db.models import F
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings
from datetime import datetime
from django.db.models import Case, Value, When
from django.db.models import Q
import json
import os


from product.models import (
	Category, 
	Product,
)
from .models import *
# Create your views here.


def add_to_cart_view(request):
	data = json.loads(request.body)
	pk = data['pk']
	action = data['action']
	pageid = data['pageid']
	
	print('Action:', action)
	print('Product:', pk)
	print('PageId:', pageid)
	if request.user.is_authenticated:
		customer = request.user.customer
		# print(customer)
		product = Product.objects.get(pk=pk)
		order, created = Order.objects.get_or_create(customer=customer, complete=False)

		orderItem, created = OrderItem.objects.get_or_create(order=order, model=product)
		done_action = {"added":False, "one_more":False, "already_added":False}

		if action == 'add' and pageid == "product-page" and created == True:
			orderItem.quantity = (orderItem.quantity + 1)
			done_action["added"] = True
	# 	# messages.success(request, f"messages now working")
	
		elif action == 'add' and pageid == "product-page" and created == False:
			done_action["already_added"] = True
	# 	messages.success(request, f"messages now working")

	# elif action == 'add' and pageId == "cart-page" and created == False and product.quantity > orderItem.quantity:
	# 	orderItem.quantity = (orderItem.quantity + 1) 
	# 	done_action["one_more"] = True

	# elif action == 'remove':
	# 	orderItem.quantity = (orderItem.quantity - 1)
	
	orderItem.save()

	if action == 'clear':
		orderItem.delete()
	
	# if orderItem.quantity <= 0:
	# 	orderItem.delete()

	return JsonResponse(done_action, safe=False, status=200)
	# return JsonResponse("done_action", safe=False, status=200)


class CartDetailView(View):
	template_name = 'shopingCard.html'
	context       = {}
	total_price = 0
	def get(self, request, *args, **kwargs):
		previous_path = self.request.GET.get('next', '')

		if request.user.is_authenticated:
			customer = self.request.user.customer
			order, created = Order.objects.get_or_create(customer=customer, complete=False)
			print("Order: ", order, '\n', "Created: ", created)
			items = order.orderitem_set.all()

			json_serializer = serializers.get_serializer("json")()
			items_json      = json_serializer.serialize(items, ensure_ascii=False)
		else:
			items = []
			items_json = dict({})
		if len(items) > 0:
			for item in items:
				if item.cart_field and item.model.discount:
					self.total_price += item.model.discount
				elif item.cart_field:
					self.total_price += item.model.price
		self.context = {
			"items":items,
			# "order":order,
			"total_price": self.total_price,
			"previous_path": previous_path,
			"items_json": items_json
		}
		return render(
			request,
			self.template_name,
			self.context,
		)



from django.core.serializers.json import DjangoJSONEncoder
from decimal import Decimal
class LazyEncoder(DjangoJSONEncoder):
	def default(self, obj):
		if isinstance(obj, Decimal):
			return str(obj)
		return super().default(obj)

def model_checkbox(request, *args, **kwargs):
	pk = request.GET.get('pk')
	action = request.GET.get('action')
	print("PrimaryKey: ", type(pk))
	if request.user.is_authenticated:
		customer = request.user.customer
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
		print("Order: ", order, '\n', "Created: ", created)
		items = order.orderitem_set.all()

		print(items)
		print(pk)
		print(action)

		if not created and len(items) > 0:
			if pk == 'all' and action=='checked':
				for item in items:
					item.cart_field = True
					print("PK: ", pk, "Value: ", item.cart_field)
					item.save()
			elif pk == 'all' and action=='unchecked':
				for item in items:
					item.cart_field = False
					print("PK: ", pk, "Value: ", item.cart_field)
					item.save()
			elif pk != '' and action != '':
				for item in items:
					if item.pk == int(pk) and item.cart_field == True:
						item.cart_field = False
						print("PK: ", pk, "Value: ", item.cart_field)
						item.save()
					elif item.pk == int(pk) and item.cart_field == False:
						item.cart_field = True
						print("PK: ", pk, "Value: ", item.cart_field)
						item.save()
	try:
		items_json = serializers.serialize('json', items, cls=LazyEncoder, ensure_ascii=True)
		return JsonResponse({"instance": items_json,}, status=200)
	except Exception as e:
		print("Error occured: ", e)
	return JsonResponse({"instance": "failed",}, status=200)