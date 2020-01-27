from django import forms

class RegistroForm(forms.Form):
	nombre = forms.CharField(max_length=100)
	apaterno = forms.CharField(max_length=100)
	amaterno = forms.CharField(max_length=100)
	telefono = forms.CharField(max_length=100)
	escuela = forms.CharField(max_length=100)
	correo = forms.CharField(max_length=100)
	password = forms.CharField(max_length=100)