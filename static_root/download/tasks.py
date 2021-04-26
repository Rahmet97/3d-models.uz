
from django.core.mail import send_mail
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404, JsonResponse, BadHeaderError
from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder
from django.template import defaultfilters
from django.conf import settings
from django.core.mail import send_mail
from django.contrib import messages
import json

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




def send_download_page(request, customer, modelid=None):
	pk   = customer.pk
	name = customer.user.first_name
	email = customer.user.email

	try:
		subject = "3D Model download link"
		if modelid:
			pk = int(modelid)
			model = Product.objects.get(pk=pk)
			order, created = OrderSingleItem.objects.get_or_create(customer=customer, model=model)
			if not created:
				order.completed = False
				order.save()
			thoughts = f"""Assalomu alekum {name}.\n Xaridingiz uchun tashakkur.
						Quyidagi link orqali siz 3d model fayl(fayllarni) yuklab olishingiz mumkin.
						http://127.0.0.1:8000/download/{pk}/{order.pk}/3d-model/zip/
						"""
		else:
			thoughts = f"""Assalomu alekum {name}.\n Xaridingiz uchun tashakkur.
						Quyidagi link orqali siz 3d model fayl(fayllarni) yuklab olishingiz mumkin.
						http://127.0.0.1:8000/download/{pk}/3d-model/zip/
						"""

		sender = settings.EMAIL_HOST_USER
		# recipients = ['dovurovjamshid95@gmail.com']
		recipients = [email, ]
		send_mail(subject, thoughts, sender, recipients, fail_silently=False)
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


