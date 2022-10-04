from django import forms
from django.utils.translation import gettext_lazy as _



class CustomLoginForm(forms.Form):
    """
    Base class for authenticating users. Extend this to get a form that accepts
    username/password logins.
    """
    phone = forms.CharField(
        max_length=12,
        widget=forms.TextInput(
            attrs={'autofocus': True, 'placeholder': 'Phone Number'}
        )
    )
    password = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                'autocomplete': 'current-password', 'placeholder': 'Password'
            }
        ),

    )

    error_messages = {
        'invalid_login': _(
            "Please enter a correct %(username)s and password. Note that both "
            "fields may be case-sensitive."
        ),
        'inactive': _("This account is inactive."),
    }
