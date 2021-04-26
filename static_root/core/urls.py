from django.urls import path

from .views import (
    MainView,
    Categories,
    ModelDetailView,
    PaymentView,
    FreeModelListView,
    download_counter,

    downloads,

    DiscuntView,
    
    PortfolioListView,
    PortfolioDetailView,

    VideosListView,

    AboutUsView,
    Contact,
    save_model, # new

    search_query,
)
from cart.views import (
    CartDetailView,
    add_to_cart_view,
    model_checkbox,
)


app_name='Core'

urlpatterns = [
    path('', MainView.as_view(), name = "main-view"),
    path('category/<int:pk>/', Categories.as_view(), name='category-view'),
    path('model/<slug:slug>/', ModelDetailView.as_view(), name='model-detail-view'),

    path('free/', FreeModelListView.as_view(), name='free-detail-view'),
    path('ajax/download_counter/', download_counter, name='download_counter'),

    path('ajax/downloads/', downloads, name='downloads'),

    path('payment/', PaymentView.as_view(), name='payment-view'),
    path('payment/<int:pk>/', PaymentView.as_view(), name='payment-view'),

    path('portfolio/', PortfolioListView.as_view(), name='portfolio-view'),
    path('portfolio/detail/<slug:slug>/', PortfolioDetailView.as_view(), name='portfolio-detail-view'),

    path('videos/', VideosListView.as_view(), name='video-view'),

    path('card/', CartDetailView.as_view(), name='card-view'),
    path('ajax/cart/detail/', add_to_cart_view, name='add_to_cart_view'),
    path('ajax/model/checkbox/', model_checkbox, name='model_checkbox'),

    path('contact/', Contact.as_view(), name='contact-view'),
    
    path('aksiya/', DiscuntView.as_view(), name='aksiya-view'),

    
    path('about/', AboutUsView.as_view(), name='about-view'),

    path('ajax/search_query/', search_query, name='search_query'),

    path('save_model/', save_model, name='save_model'), # new
]
