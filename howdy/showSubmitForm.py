# myclub_root\myclub_site\contact.py

from django import forms

class ContactForm(forms.Form):
    showname = forms.CharField(max_length=100, label='Show Name')
    