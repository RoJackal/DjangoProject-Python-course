from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Please enter your username'
        self.fields['password'].widget.attrs['placeholder'] = 'Please enter your password'

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields =['first_name', 'last_name', 'username', 'email']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['class'] = 'form-control'
        self.fields['last_name'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['first_name'].widget.attrs['placeholder'] = 'Please enter your first name'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Please enter your last name'
        self.fields['username'].widget.attrs['placeholder'] = 'Please enter your username'
        self.fields['email'].widget.attrs['placeholder'] = 'Please enter your email'
        self.fields['password1'].widget.attrs['placeholder'] = 'Please enter your password'
        self.fields['password2'].widget.attrs['placeholder'] = 'Please enter your password confirmation'
