from django import forms
from .models import recipients

class RecipientRegistrationForm(forms.ModelForm):
    class Meta:
        model = recipients
        fields = ['full_name', 'email', 'contact_number', 'date_of_birth', 'gender', 'blood_group', 'organ_needed', 'address']
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
        }
