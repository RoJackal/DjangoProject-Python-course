from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError
from manager.models import Manager
GENDER_OPTIONS = [
	('male', 'Male'),
	('female', 'Female'),
	]
class Employee(models.Model):
	first_name = models.CharField(max_length=30, db_index=True)
	last_name = models.CharField(max_length=30, db_index=True)
	email = models.EmailField(max_length=50, unique=True, null=True, blank=True, db_index=True)
	age = models.PositiveIntegerField(
			validators=[MinValueValidator(18), MaxValueValidator(100)]
			)
	salary = models.DecimalField(
			max_digits=10,
			decimal_places=2,
			validators=[MinValueValidator(0)]
			)
	gender = models.CharField(choices=GENDER_OPTIONS, max_length=6)
	hire_date = models.DateField(db_index=True)
	active = models.BooleanField(default=True, db_index=True)
	manager = models.ForeignKey(
			Manager,
			on_delete=models.CASCADE,
			null=True,
			blank=True,
			related_name='employees'
			)
	# Auxiliary fields
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	
	class Meta:
		ordering = ['-hire_date', 'last_name', 'first_name']
		indexes = [
			models.Index(fields=['last_name', 'first_name']),
			models.Index(fields=['active', 'hire_date']),
			models.Index(fields=['manager', 'active']),
			]
		verbose_name = 'Employee'
		verbose_name_plural = 'Employees'
	
	def __str__( self ):
		return f'{self.first_name} {self.last_name}'
	def clean( self ):
		"""Validate model fields"""
		super().clean()
		
		# Validate age
		if self.age and (self.age < 18 or self.age > 100):
			raise ValidationError({ 'age': 'Age must be between 18 and 100' })
		
		# Validate salary
		if self.salary and self.salary < 0:
			raise ValidationError({ 'salary': 'Salary cannot be negative' })
	def save( self, *args, **kwargs ):
		"""Override save to call full_clean"""
		self.full_clean()
		super().save(*args, **kwargs)
	@property
	def full_name( self ):
		"""Return full name"""
		return f'{self.first_name} {self.last_name}'
	@property
	def is_senior( self ):
		"""Check if employee has been with company for 5+ years"""
		from datetime import date
		from dateutil.relativedelta import relativedelta
		
		years_employed = relativedelta(date.today(), self.hire_date).years
		return years_employed >= 5
