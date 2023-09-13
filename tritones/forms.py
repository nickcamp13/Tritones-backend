from django import forms
from .models import ContactSubmission


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactSubmission
        fields = ['name', 'subject', 'email', 'message']