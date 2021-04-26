from django import forms
from django.utils.translation import gettext_lazy as _

class SearchForm(forms.Form):
	search_query = forms.CharField(
		max_length=300, widget=forms.TextInput(
			attrs={
			"type":"text",
			"id":"search_input_field",
			"name":"search", 
			"placeholder":_("Qidirish")}, 
		),
		required=True
	)
