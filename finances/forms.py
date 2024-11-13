# finances/forms.py
from django import forms
from .models import Transaction, Budget

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['category', 'description', 'amount']

class BudgetForm(forms.ModelForm):
    class Meta:
        model = Budget
        fields = ['category', 'amount', 'start_date', 'end_date']
