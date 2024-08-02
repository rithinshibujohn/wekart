from django import forms

class ProductSearchForm(forms.Form):
    query = forms.CharField(label='Search', max_length=255)
