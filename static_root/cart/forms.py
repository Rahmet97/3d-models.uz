from django import forms
from django.forms.widgets import TextInput


class PayForm(forms.Form):
    number = forms.CharField(
        max_length=19,
        widget=TextInput(attrs={
            'class': 'payment__input',
            'id': 'card',
            'name': 'card',
            'onkeyup': 'space()',
            'placeholder': '**** **** **** ****'
        })
    )
    exp_date = forms.CharField(
        max_length=5,
        required=True,
        widget=TextInput(attrs={
            'class': 'payment__input',
            'id': 'data',
            'name': 'data',
            'placeholder': '00/00'
        })
    )
    