from django import forms


class Home(forms.Form):
    search_box = forms.CharField(label='Search', widget=forms.TextInput(attrs={'placeholder': 'Ask me anything'}))

