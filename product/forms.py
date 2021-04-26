from django import forms
from django.utils.translation import gettext_lazy as _

class ModelSearchForm(forms.Form):
	search_query = forms.CharField(
		max_length=300, widget=forms.TextInput(attrs={"placeholder":_("Qidiruv...")})
	)