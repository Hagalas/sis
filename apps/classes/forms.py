# -*- coding: utf-8 -*-
from django import forms

from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext, ugettext_lazy as _


class AuthForm(AuthenticationForm):
    username = forms.CharField(label=_("Login"), max_length=254)
    password = forms.CharField(label=_(u"Hasło"), widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super(AuthForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['class'] = 'form-control'