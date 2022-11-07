from django.forms import ModelForm
from .models import Account
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from pages.models import Code
from django.shortcuts import get_object_or_404

class CodeForm(forms.ModelForm):
    number = forms.CharField(label = 'Code', help_text='Enter SMS verifiation code')
    class Meta:
        model = Code
        fields = ('number',)

class AccountForm(ModelForm):
    class Meta:
        model = Account
        fields = ['email', 'first_name', 'last_name', 'country', 'password']
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

form = AccountForm()
one_account = Account()
print(one_account.get_user())

#article = get_object_or_404(Account, pk=1)
#article = Account.objects.get(pk=1)
#form = AccountForm(instance=article)