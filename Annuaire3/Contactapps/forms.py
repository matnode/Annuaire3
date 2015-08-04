from django import forms

class ContactForm(forms.Form):
	photo = forms.ImageField()
