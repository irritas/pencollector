from django.forms import ModelForm
from .models import Refill

class RefillForm(ModelForm):
    class Meta:
        model = Refill
        fields = ['date', 'color']
