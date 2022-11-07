from django import forms
from pages.models import Code
class CodeForm(forms.ModelForm):
    number = forms.CharField(label = 'Code', help_text='Enter SMS verifiation code')
    class Meta:
        model = Code
        fields = ('number',)