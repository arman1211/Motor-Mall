from . import models
from django import forms

class CarForm(forms.ModelForm):
    class Meta:
        model = models.CarModel
        fields = '__all__'