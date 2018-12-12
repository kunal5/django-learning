from django import forms


class Login(forms.Form):
    username = forms.CharField(max_length=30, required=True, label='User Name')
    password = forms.CharField(widget=forms.widgets.PasswordInput(), required=True, label='Password')
