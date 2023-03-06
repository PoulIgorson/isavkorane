from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from main.models import User


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label='Логин',
        widget=forms.TextInput(
            attrs={
                'class': 'form-input',
                'placeholder': 'Введите имя пользователя'
            }
        )
    )
    password = forms.CharField(
        label='Введите пароль',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-input',
                'placeholder': 'Введите пароль'
            }
        )
    )

    class Meta:
        model = User
        fields = ('username', 'password')


class RegistrationForm(UserCreationForm):
    username = forms.CharField(
        label='Логин',
        widget=forms.TextInput(
            attrs={
                'class': 'form-input',
                'placeholder': 'Введите имя пользователя'
            }
        )
    )
    password1 = forms.CharField(
        label='Создайте пароль',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-input',
                'placeholder': 'Введите пароль'
            }
        )
    )
    password2 = forms.CharField(
        label='Подтвердите пароль',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-input',
                'placeholder': 'Повторите пароль'
            }
        )
    )

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')


class CreatePageForm(forms.Form):
    name = forms.CharField(label='Название страницы')
    header = forms.CharField(label='Заголовок')
