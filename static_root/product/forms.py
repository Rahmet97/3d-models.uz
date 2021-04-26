from django import forms

class ModelSearchForm(forms.Form):
	search_query = forms.CharField(
		max_length=300, widget=forms.TextInput(attrs={"placeholder":"Search..."})
	)