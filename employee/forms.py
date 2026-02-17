from django import forms

from employee.models import Employee
class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your first name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your last name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your email'}),
            'age': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your age'}),
            'salary': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your salary'}),
            'hire_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'gender': forms.Select(attrs={'class': 'form-select'}),
            'manager': forms.Select(attrs={'class': 'form-select'}),
        }
        def clean( self ):
            cleaned_data = self.cleaned_data
            
            # O validare prin care adresa de email sa fie unica.
            get_email = cleaned_data.get('email')
            check_emails = Employee.objects.filter(email=get_email)
            if check_emails:
                msg = 'Email already registered.'
                self.add_error('email', msg)
            
            # Validare pentru ca first_name si last_name sa fie unic
            check_fname = cleaned_data.get('first_name')
            check_lname = cleaned_data.get('last_name')
            check_fname_lname = Employee.objects.filter(first_name=check_fname, last_name=check_lname)
            if check_fname_lname:
                msg = 'First name and Last name already registered'
                self.add_error('first_name', msg)
                self.add_error('last_name', msg)
            
            # Validare ca varsta sa fie minim 18 ani
            check_age = cleaned_data.get('age')
            if check_age < 18:
                msg = 'Age must be over 18!'
                self.add_error('age', msg)
            
            # Validare in care data angajarii sa fie mai mica  sau egal decat ziua curenta
            check_date = cleaned_data.get('hire_date')
            if check_date > datetime.date.today():
                msg = 'Invalid hire date'
                self.add_error('hire_date', msg)
            
            return cleaned_data
class EmployeeUpdateForm(forms.ModelForm):
	class Meta:
		model = Employee
		fields = ["email", "age", "manager", "active"]
		
		widgets = {
			# 'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your first name'}),
			# 'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your last name'}),
			"email":   forms.EmailInput(
					attrs={
						"class":       "form-control",
						"placeholder": "Please enter your email",
						}
					),
			"age":     forms.NumberInput(
					attrs={ "class": "form-control", "placeholder": "Please enter your age" }
					),  # 'salary': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your salary'}),
			# 'gender': forms.Select(attrs={'class': 'form-select'}),
			# 'hire_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
			"manager": forms.Select(attrs={ "class": "form-select" }),
			}
