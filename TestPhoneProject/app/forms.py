from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _
from phonenumber_field.formfields import PhoneNumberField

from .models import User



class CustomUserCreationForm(UserCreationForm):
    phone = PhoneNumberField(region='KZ', label=_('Phone Number'))

    class Meta:
        model = User
        fields = ('phone',)

