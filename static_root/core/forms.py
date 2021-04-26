from django import forms

class SearchForm(forms.Form):
	search_query = forms.CharField(
		max_length=300, widget=forms.TextInput(
			attrs={
			"type":"text",
			"id":"search_input_field",
			"name":"search", 
			"placeholder":"Qidirish"}, 
		),
		required=True
	)
