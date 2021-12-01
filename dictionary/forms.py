from django import forms
from .models import DictionaryModel
class DictionaryForm(forms.ModelForm):
    
    class Meta:
        model = DictionaryModel
        fields = ['word', 'defination']
    