from django import forms
from database.models import Transaction

class BudgetImportForm(forms.ModelForm):

    class Meta:
        model = Transaction
        fields = ()