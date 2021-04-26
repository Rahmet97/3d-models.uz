from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth import password_validation
from django.core.validators import RegexValidator
from django.contrib.auth.forms import UserCreationForm


from django.contrib.auth.forms import AuthenticationForm

User = get_user_model()

class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)
    username = forms.EmailField(widget=forms.EmailInput(attrs={"type":"email", "name":"email", "placeholder":"Email", "class":"form__input"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"type":"pasword", "name":"password", "placeholder":"password", "class":"form__input",}))

class NewUserForm(UserCreationForm):
	email = forms.EmailField(
        required=True,
        label="Адрес электронной почты",
        widget=forms.EmailInput(attrs={"type":"email", "class":"form__input", "id":"email", "name":"email", "placeholder":"Elektron pochta",}), #class="form__input" id="email" name="email" type="email" placeholder="Elektron pochta"
    )

	first_name = forms.CharField(
        required=True,
        label="Имя пользователя",
        widget=forms.TextInput(attrs={"type":"text", "class":"form__input", "id":"Name", "name":"Name", "placeholder":"FISH",}), #class="form__input" id="Name" name="Name" type="text" placeholder="IFSH"
    )

	phone_regex = RegexValidator(regex=r'^\+?998?\d{9,15}$', message="Phone number must be entered in the format: '+998000000000'. Up to 12 digits allowed.")
	phone_number = forms.CharField(validators=[phone_regex], 
        label="Телефонный номер",
        widget=forms.TextInput(
            attrs={"type":"text", "class":"form__input", "name":"text", "placeholder":"Telefon Raqam",}), #class="form__input" id="text" name="text" type="text" placeholder="Telefon Raqam"
    )

	password1 = forms.CharField(
        label="Пароль",
        # strip=False,
        widget=forms.PasswordInput(
            attrs={"type":"password", "class":"form__input", "id":"password", "name":"password", "placeholder":"Parol",}), #class="form__input" id="password" name="password" type="password" placeholder="Parol"
        help_text=password_validation,
    )
    
	password2 = forms.CharField(
        label="Подтвердить пароль",
        # strip=False,
        widget=forms.PasswordInput(
            attrs={"type":"password", "class":"form__input", "id":"password1", "name":"password1", "placeholder":"Parolni Tasdiqlash",}), #class="form__input" id="password1" name="password" type="password" placeholder="Parol tasdiqlash"
        help_text=password_validation,
    )
	class Meta:
		model=User
		fields = ("email", "first_name", "phone_number", "password1", "password2")
    
	def clean(self):
		cleaned_data=self.cleaned_data
		password_1=self.cleaned_data.get('password1')
		password_2=self.cleaned_data.get('password2')
		if password_1 != password_2:
			raise forms.ValidationError("Пароль не совпадал. Попробуйте назад")
		return cleaned_data
    
	def clean_email(self):
		email_address=self.cleaned_data.get('email')
		queryset=User.objects.filter(email=email_address)
		if queryset.exists():
			raise forms.ValidationError('Выбранный вами адрес электронной почты уже зарегистрирован')
		return email_address
	
	def clean_phone_number(self):
		phone_number=self.cleaned_data.get('phone_number')
		queryset=User.objects.filter(phone_number=phone_number)
		if queryset.exists():
			raise forms.ValidationError('Этот номер телефона уже зарегистрирован')
		return phone_number

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
       
		if commit:
			user.save()
		return user





class FeedbackForm(forms.Form):
    first_name   = forms.CharField(
                 max_length=25,
                 widget=forms.TextInput(
                        attrs={
                            'class': 'contact__input',
                            'type': "text",
                            'id'  : "Name",
                            'name': "Name",
                            'placeholder': "Ismingizni kiriting",
                            # required
                        }
                     )
                 )
    last_name    = forms.CharField(
                 max_length=25,
                 widget=forms.TextInput(
                        attrs={
                            'class': 'contact__input',
                            'type': "text",
                            'id'  : "surname",
                            'name': "surname",
                            'placeholder': "Familiyangizni kiriting",
                            # required
                        }
                     )
                 )
    phone_number = forms.CharField(
                 max_length=13,
                 widget=forms.TextInput(
                        attrs={
                            'class': "contact__input",
                            'type': "text",
                            'id'  : "number",
                            'name': "number",
                            'placeholder': "Telefon Raqamingizni kiriting",
                            # required
                        }
                     )
                 )
    text         = forms.CharField(
                 widget=forms.Textarea(
                        attrs={
                            'class': "contact__input",
                            'id': "textr",
                            'rows':"5",
                            'cols': "10",
                            "name": "",
                            "placeholder" : "Fikir mulohaza va takliflaringizni kiriting"
                        }
                    )
                 )