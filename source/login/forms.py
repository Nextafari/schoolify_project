from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    email = forms.EmailField(label='Email', max_length=250)
    password = forms.CharField(max_length=40, widget=forms.PasswordInput)