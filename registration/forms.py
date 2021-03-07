from django.db.models import fields
from . import models
from django import forms

class Apply(forms.ModelForm):
    class Meta:
        model = models.Application
        fields = [ 'name', 'department', 'email' ]
