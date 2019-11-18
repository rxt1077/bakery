from django import forms

class BakerForm(forms.Form):
    cookie_name = forms.CharField(label='Cookie Name', max_length=100)
    amount = forms.IntegerField()