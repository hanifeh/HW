from django import forms
from . import models


class UserForm(forms.ModelForm):

    class Meta:
        model = models.MyUser
        fields = [
            'first_name',
            'last_name',
            'phone_number',
        ]
