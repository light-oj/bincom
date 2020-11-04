from django import forms
from .models import PollingUnit

class PollingResultForm(forms.ModelForm):
    class Meta:
        model= PollingUnit
        fields = ('__all__')