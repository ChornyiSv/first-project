from django import forms
from Store.models import CreateProduct
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# форма створенні продукту через фронтенд частину
class CreateProductForm(forms.ModelForm):
    class Meta:
        model = CreateProduct
        fields = [
            'title',
            'image',
            'topic',
            'description',
            'price',
            'site'
        ]

# форма логування через фронтенд частину
class LoginForm(forms.Form):
    login = forms.CharField(label='Username', max_length=16)
    password = forms.CharField(label='Password', widget=forms.PasswordInput(), max_length=25)

# форма реєстрації через фронтенд частину
class RegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2'
        ]