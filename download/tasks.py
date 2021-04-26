
from django.core.mail import send_mail
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404, JsonResponse, BadHeaderError
from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder
from django.template import defaultfilters
from django.conf import settings
from django.core.mail import send_mail, EmailMultiAlternatives
from django.contrib import messages
import json
from django.utils.translation import gettext_lazy as _
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.utils.crypto import get_random_string

import os
import zipfile
try:
	from StringIO import StringIO
except ImportError:
	from io import StringIO

from cart.models import OrderSingleItem
from product.models import Product

from io import BytesIO

def zip_maker(filelist, customer):
	pk = customer.pk
	name = customer.user.first_name

	byte_data = BytesIO()
	zip_file = zipfile.ZipFile(byte_data, "w")

	for file in filelist:
		filename = os.path.basename(os.path.normpath(file))
		zip_file.write(file, filename)
	zip_file.close()

	response = HttpResponse(byte_data.getvalue(), content_type='application/zip')
	response['Content-Disposition'] = f'attachment; filename={name}{pk}_3d_model_files.zip'

	zip_file.printdir()

	return response

# file:///home/jamshid/Instant%20Company/3D%20Marketing/3d_model_backend_raximjon_aka/3d_models/media/3D_File/2021/02/25/IMG_20180131_235840_953_2.jpg
# file:///home/jamshid/Instant%20Company/3D%20Marketing/3d_model_backend_raximjon_aka/3d_models/media_root/3D_File/2021/02/25/IMG_20180131_235840_953_2.jpg


link = ''

def send_download_page(request, customer, modelid=None):
	pk   = customer.pk
	name = customer.user.first_name
	email = customer.user.email

	uri = request.build_absolute_uri().split('/')
	domain = uri[0]+'//'+uri[2]+'/'+uri[3]+'/'
	
	try:
		subject = _("3D Model yuklash havolasi")
		global link
		if modelid:
			pk = int(modelid)
			model = Product.objects.get(pk=pk)
			order, created = OrderSingleItem.objects.get_or_create(customer=customer, model=model)
			if not created:
				order.completed = False
				order.save()
			print(request.path)
			# link = "http://www.3d-models.uz" + request.path[:3] + "/download/" + pk + "/" + order.pk + "/3d-model/zip/"
			link = domain + "download/" + str(pk) + "/" + str(order.pk) + "/3d-model/zip/"
		else:
			print(request.path)
			# link = "http://www.3d-models.uz" + request.path[:3] + "/download/" + pk + "/3d-model/zip/"
			link = domain + "download/" + str(pk)+ "/3d-model/zip/"
		
		token_address = get_random_string(length=32)
		address = domain + "download/" + token_address
		html_message = render_to_string('email.html', {'token_address': address})
		thoughts = strip_tags(html_message)


		sender = settings.EMAIL_HOST_USER
		# recipients = ['dovurovjamshid95@gmail.com']
		recipients = [email]
		email_msg = EmailMultiAlternatives(
			subject,
			thoughts,
			sender,
			recipients
		)
		email_msg.attach_alternative(html_message, 'text/html')
		email_msg.send()
		# send_mail(subject, sender, recipients, html_message=html_message, fail_silently=False)
		# messages.success(request, f"{name} xabaringiz muvofaqiyatli yuborildi.")
	except Exception as e:
		print("Houston, we have a problem! :(\n", e )



"""
from celery import shared_task
import os  
from zipfile import ZipFile, ZIP_DEFLATED



@shared_task
def get_zip_file(request, file_paths):

	# Folder name in ZIP archive which contains the above files
	# E.g [thearchive.zip]/somefiles/file2.txt
	# FIXME: Set this to something better
	zip_subdir = "somefiles"
	zip_filename = "%s.zip" % zip_subdir


	# The zip compressor
	zf = ZipFile(zip_filename, "w")

	for fpath in file_paths:
		# Calculate path for file in zip
		fdir, fname = os.path.split(fpath)
		zip_path = os.path.join(zip_subdir, fname)

		# Add file, at correct path
		zf.write(fpath, compress_type=ZIP_DEFLATED)

	# Must close zip for all contents to be written
	zf.close()
"""


