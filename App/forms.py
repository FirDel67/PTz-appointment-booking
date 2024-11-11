from django import forms
from .models import CustomUser

class UpdatePatientForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'address', 'username']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'w-full px-4 py-2 border rounded-lg'}),
            'last_name': forms.TextInput(attrs={'class': 'w-full px-4 py-2 border rounded-lg'}),
            'email': forms.EmailInput(attrs={'class': 'w-full px-4 py-2 border rounded-lg'}),
            'phone_number': forms.TextInput(attrs={'class': 'w-full px-4 py-2 border rounded-lg'}),
            'address': forms.TextInput(attrs={'class': 'w-full px-4 py-2 border rounded-lg'}),
            'username': forms.TextInput(attrs={'class': 'w-full px-4 py-2 border rounded-lg'}),
        }
