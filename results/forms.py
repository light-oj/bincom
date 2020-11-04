from django import forms
from .models import PollingUnit, AnnouncedPuResults

class PollingResultForm(forms.ModelForm):
    class Meta:
        model= PollingUnit
        fields = ('__all__')

class AnnouncedPuResultsForm(forms.ModelForm):
    class Meta:
        model= AnnouncedPuResults
        fields = (
            'polling_unit_uniqueid',
            'party_abbreviation',
            'party_score',
            'entered_by_user',
            'user_ip_address',)