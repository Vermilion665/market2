from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UsernameField

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput, error_messages={'required': 'Пжлст, заполните поле'})
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')
        help_texts = {
            'username': 'Only strings, numbers and @/,/+/-/_',
        }

        labels = {
            'username': 'Логин',
            'first_name': 'Имя пользователя',
            'email': 'Эл. почта',
        }

        widgets = {
            'username': forms.TextInput,
            'email': forms.EmailInput,
            'first_name': forms.TextInput,
        }
        # error_messages = {
        #     'username': {
        #         'required': 'Это поле обязательно для заполнения',
        #     },

        #     'password': {
        #         'required': 'Это поле обязательно для заполнения',
        #     },
        # }

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Пароли не совпадают!!!')
        return cd['password2']

class AuthForm(AuthenticationForm):
    username = UsernameField(label='Логин', widget=forms.TextInput(attrs={"autofocus": True}))
    password = forms.CharField(
        label=_("Пароль"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "current-password"}),
    )

    error_messages = {
        "invalid_login": _(
            "Пжлст введите корректные логин и пароль."
        ),
        "inactive": _("Этот аккаунт заблокирован."),
    }