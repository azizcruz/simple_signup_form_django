from django import forms
from .models import TinyForm

class TinyTestForm(forms.ModelForm):
    class Meta:
        model = TinyForm
        fields = ('username', 'email')
