from django import forms


class SignUp(forms.Form):
    username = forms.CharField(max_length=30, required=True, label='User Name')
    first_name = forms.CharField(max_length=30, required=True, label='First Name')
    last_name = forms.CharField(max_length=30, required=False, label='Last Name')
    password = forms.CharField(widget=forms.widgets.PasswordInput(), required=True, label='Password')
    email = forms.EmailField(label='Email')
