from django.urls import  reverse_lazy
from django.views.generic import CreateView
# from django.contrib.auth.forms import UserCreationForm


from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.http import HttpResponse, Http404, HttpResponseRedirect ,BadHeaderError
from django.views import View

# from django.contrib.auth.forms import  AuthenticationForm  # Now we can use 'LoginForm' instead of 'AuthenticationForm'
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from .forms import FeedbackForm
from django.core.mail import send_mail
from django.conf import settings
# from shumoff import settings

from .forms import NewUserForm, UserLoginForm
# from core.models  import Category
# Create your views here.


class NewUserCreationForm(SuccessMessageMixin, CreateView):
    template_name = 'registration/register.html'
    form_class = NewUserForm
    success_url = reverse_lazy('login')
    success_message = "New account for %(first_name)s was created successfully"
   
    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            first_name=self.object.first_name,
        )


class LoginFormView(SuccessMessageMixin, LoginView):
    template_name="registration/login.html"
    authentication_form=UserLoginForm
    # template_name = 'auth/login.html'
    success_url = reverse_lazy('/')
    success_message = "Email %(username)s were successfully logged in."

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            username=self.object.username,
        )



def logout(request):
	logout(request)
	messages.info(request, "Logged out successfully!")
	return redirect("Products:product-list")


