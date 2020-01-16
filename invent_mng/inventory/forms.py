from django import forms

from .models import *


class Item1Form(forms.ModelForm):
    class Meta:
        model = Item1
        fields = ('type', 'price', 'status', 'issues')


class Item2Form(forms.ModelForm):
    class Meta:
        model = Item2
        fields = ('type', 'price', 'status', 'issues')


class Item3Form(forms.ModelForm):
    class Meta:
        model = Item3
        fields = ('type', 'price', 'status', 'issues')
