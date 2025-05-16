#!/usr/bin/python
from django import forms
from database.models import Transaction

class EditTransaction(forms.Form):
    charge_date = forms.DateField(label="Charge Date")
    charge_name = forms.CharField(label="Charge Name", max_length=250)
    charge_amount = forms.FloatField(label="Charge Amount")
    charge_category = forms.CharField(label="Category", max_length=50, required=False)
    charge_notes = forms.CharField(label="Notes", max_length=250, required=False)
    
