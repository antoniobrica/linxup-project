from django import forms
from .models import UserProfile

class FirstForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['last_name', 'first_name', 'zip_code', 'city', 'email', 'phone', 'birthdate', 'linkedin']

class SecondForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['branch', 'job_title', 'experience', 'satisfaction', 'education', 'skills']
