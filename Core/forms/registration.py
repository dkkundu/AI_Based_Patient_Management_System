"""Core > forms > registration.py"""
# DJANGO IMPORTS
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms

USER_MODEL = get_user_model()


class SignupForm(UserCreationForm):
    """New user registration and signup form"""

    class Meta:
        """Meta class"""
        model = USER_MODEL
        fields = ('first_name', 'last_name', 'email', 'phone')


class CommonSignupForm(UserCreationForm):
    """New user registration and signup form"""

    class Meta:
        """Meta class"""
        model = USER_MODEL
        fields = [
            'phone'
        ]

    def __init__(self, *args, **kwargs):
        super(CommonSignupForm, self).__init__(*args, **kwargs)
        self.fields["phone"].required = True


class UpdateForm(forms.ModelForm):
    class Meta:
        """Meta class"""
        model = USER_MODEL
        fields = ('first_name', 'last_name', 'phone',)
