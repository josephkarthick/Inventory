from django import forms
from .models import product

class pro(models.ModelForm):
    class meta:
        model = product
        fields = '__all__'