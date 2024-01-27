# worker/forms.py
from django import forms
from .models import Worker

class WorkerRegistrationForm(forms.ModelForm):
    class Meta:
        model = Worker
        fields = ['name', 'phone_number', 'address', 'email', 'key_skills', 'availability']

class WorkerUpdateForm(forms.ModelForm):
    class Meta:
        model = Worker
        fields = ['phone_number', 'address', 'email', 'key_skills', 'availability']
