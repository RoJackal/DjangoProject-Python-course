from django import forms
from manager.models import Manager


class ManagerForm(forms.ModelForm):
    class Meta:
        model = Manager
        fields = '__all__'  # fieldurile pe care le dorim in formular
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your first name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your last name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your email'}),
            'department': forms.Select(attrs={'class': 'form-select'}),
            'hire_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }
