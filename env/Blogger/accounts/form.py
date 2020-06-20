from django import forms
from blog.models import Post
from .models import Country,City,State,Account

class LoginForm(forms.Form):
    Email = forms.EmailField(widget=forms.EmailInput)
    Password = forms.CharField(widget=forms.PasswordInput)

class CountryForm(forms.ModelForm):
    class Meta:
        model=Country
        fields='__all__'

class StateForm(forms.ModelForm):
    class Meta:
        model=State
        fields='__all__'

class CityForm(forms.ModelForm):
    class Meta:
        model=City
        fields='__all__'

class AccountForm(forms.ModelForm):
    class Meta:
        model=Account
        fields='__all__'
        widgets={
            'password':forms.PasswordInput(),
        }

class EditAccountForm(forms.ModelForm):
    class Meta:
        model=Account
        fields='__all__'
        exclude = ['password']


class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields='__all__'



class SearchForm(forms.ModelForm):
    search = forms.CharField(required=False,widget=forms.TextInput(attrs={'placeholder':'Search',}))

class CountrySearch(forms.ModelForm):
    class Meta:
        model=Country
        fields=['name']
        widgets = {
            'name':forms.TextInput(attrs={'placeholder':'Search',})
        }