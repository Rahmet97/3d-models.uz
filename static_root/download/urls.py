from django.urls import path
from . import views

app_name='download'

urlpatterns = [
    path('card_verify_code', views.card_verify_code, name="card_verify_code"),
    path('<int:pk>/3d-model/zip/', views.make_models_zip, name='zip'),
    path('<int:pk>/<int:os_pk>/3d-model/zip/', views.make_models_zip, name='zip'),
]