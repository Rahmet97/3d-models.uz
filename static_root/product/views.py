from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import F
import json
from django.views.generic import (
    ListView,
    DetailView,
)

from .models import (
    Category,
    Product,
    Images,
) 
# Create your views here.


# Download counter
def download_counter(request):
    Product.objects.filter(slug = request.GET.get('request_data')).update(downloaded = F('downloaded')+1)
    return HttpResponse(
        json.dumps('Increased'),
        content_type="application/json"
    )