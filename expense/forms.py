from django import forms
from django.contrib.auth.models import User


from .models import Account, Category, Transactions


class UserForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class BudgetForm(forms.ModelForm):

    class Meta:
        model = Account
        fields = ['monthly_budget']


class AccountForm(forms.ModelForm):
    """docstring for AccountForm"""

    class Meta:
        model = Transactions
        fields = ['amount', 'category', 'transaction_type', 'comment','account']