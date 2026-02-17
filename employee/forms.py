import datetime
from django import forms
from django.core.exceptions import ValidationError

from employee.models import Employee
class EmployeeForm(forms.ModelForm):
	"""Form for creating new employee"""
	
	class Meta:
		model = Employee
		fields = '__all__'
		
		widgets = {
			'first_name': forms.TextInput(attrs={
				'class':       'form-control',
				'placeholder': 'Please enter first name'
				}
					),
			'last_name':  forms.TextInput(attrs={
				'class':       'form-control',
				'placeholder': 'Please enter last name'
				}
					),
			'email':      forms.EmailInput(attrs={
				'class':       'form-control',
				'placeholder': 'Please enter email'
				}
					),
			'age':        forms.NumberInput(attrs={
				'class':       'form-control',
				'placeholder': 'Please enter age (18-100)',
				'min':         '18',
				'max':         '100'
				}
					),
			'salary':     forms.NumberInput(attrs={
				'class':       'form-control',
				'placeholder': 'Please enter salary',
				'step':        '0.01',
				'min':         '0'
				}
					),
			'hire_date':  forms.DateInput(attrs={
				'class': 'form-control',
				'type':  'date',
				'max':   datetime.date.today().isoformat()
				}
					),
			'gender':     forms.Select(attrs={ 'class': 'form-select' }),
			'manager':    forms.Select(attrs={ 'class': 'form-select' }),
			'active':     forms.CheckboxInput(attrs={ 'class': 'form-check-input' }),
			}
	
	def clean_email( self ):
		"""Validate email uniqueness"""
		email = self.cleaned_data.get('email')
		
		if email:
			# Check if email already exists (excluding current instance for updates)
			existing = Employee.objects.filter(email=email)
			if self.instance.pk:
				existing = existing.exclude(pk=self.instance.pk)
			
			if existing.exists():
				raise ValidationError('Email already registered.')
		
		return email
	def clean_age( self ):
		"""Validate age is at least 18"""
		age = self.cleaned_data.get('age')
		
		if age and age < 18:
			raise ValidationError('Age must be at least 18 years.')
		
		if age and age > 100:
			raise ValidationError('Age must be less than 100 years.')
		
		return age
	def clean_salary( self ):
		"""Validate salary is positive"""
		salary = self.cleaned_data.get('salary')
		
		if salary and salary < 0:
			raise ValidationError('Salary cannot be negative.')
		
		return salary
	def clean_hire_date( self ):
		"""Validate hire date is not in the future"""
		hire_date = self.cleaned_data.get('hire_date')
		
		if hire_date and hire_date > datetime.date.today():
			raise ValidationError('Hire date cannot be in the future.')
		
		return hire_date
	def clean( self ):
		"""Additional validation for first_name and last_name combination"""
		cleaned_data = super().clean()
		
		first_name = cleaned_data.get('first_name')
		last_name = cleaned_data.get('last_name')
		
		if first_name and last_name:
			# Check if combination already exists (excluding current instance)
			existing = Employee.objects.filter(
					first_name=first_name,
					last_name=last_name
					)
			
			if self.instance.pk:
				existing = existing.exclude(pk=self.instance.pk)
			
			if existing.exists():
				raise ValidationError(
						'An employee with this first name and last name combination already exists.'
						)
		
		return cleaned_data
class EmployeeUpdateForm(forms.ModelForm):
	"""Form for updating existing employee (limited fields)"""
	
	class Meta:
		model = Employee
		fields = ["email", "age", "salary", "manager", "active"]
		
		widgets = {
			"email":   forms.EmailInput(attrs={
				"class":       "form-control",
				"placeholder": "Please enter email",
				}
					),
			"age":     forms.NumberInput(attrs={
				"class":       "form-control",
				"placeholder": "Please enter age",
				"min":         "18",
				"max":         "100"
				}
					),
			"salary":  forms.NumberInput(attrs={
				"class":       "form-control",
				"placeholder": "Please enter salary",
				"step":        "0.01",
				"min":         "0"
				}
					),
			"manager": forms.Select(attrs={ "class": "form-select" }),
			"active":  forms.CheckboxInput(attrs={ "class": "form-check-input" }),
			}
	
	def clean_email( self ):
		"""Validate email uniqueness"""
		email = self.cleaned_data.get('email')
		
		if email:
			existing = Employee.objects.filter(email=email).exclude(pk=self.instance.pk)
			if existing.exists():
				raise ValidationError('Email already registered.')
		
		return email
	def clean_age( self ):
		"""Validate age"""
		age = self.cleaned_data.get('age')
		
		if age and (age < 18 or age > 100):
			raise ValidationError('Age must be between 18 and 100 years.')
		
		return age
	def clean_salary( self ):
		"""Validate salary is positive"""
		salary = self.cleaned_data.get('salary')
		
		if salary and salary < 0:
			raise ValidationError('Salary cannot be negative.')
		
		return salary
