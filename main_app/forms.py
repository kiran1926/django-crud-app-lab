from django import forms
from .models import Watering, Fertilizer

class WateringForm(forms.ModelForm):
    class Meta:
        model = Watering
        fields = ['date', 'amount', 'notes']
        widgets = {
            'date': forms.DateInput(
                format=('%Y-%m-%d'),
                attrs={
                    'placeholder': 'Select a date',
                    'type': 'date'
                }
            ),
        }

class FertilizerForm(forms.ModelForm):
    class Meta:
        model = Fertilizer
        fields = ['date', 'type', 'amount', 'notes']
        widgets = {
            'date': forms.DateInput(
                format=('%Y-%m-%d'),
                attrs={
                    'placeholder': 'Select a date',
                    'type': 'date'
                }
            ),
        } 