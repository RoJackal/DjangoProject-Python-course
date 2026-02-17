from django.db import models
class Manager(models.Model):
	"""Manager model with department assignment"""
	
	DEPARTMENT_OPTIONS = [
		('hr', 'Human Resources'),
		('it', 'Information Technology'),
		('sales', 'Sales'),
		('marketing', 'Marketing'),
		('finance', 'Finance'),
		]
	
	first_name = models.CharField(max_length=40, db_index=True)
	last_name = models.CharField(max_length=40, db_index=True)
	email = models.EmailField(max_length=60, unique=True, db_index=True)
	department = models.CharField(max_length=20, choices=DEPARTMENT_OPTIONS, db_index=True)
	hire_date = models.DateField()
	active = models.BooleanField(default=True)
	
	# Timestamps
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	
	class Meta:
		ordering = ['department', 'last_name', 'first_name']
		indexes = [
			models.Index(fields=['department', 'active']),
			models.Index(fields=['last_name', 'first_name']),
			]
		verbose_name = 'Manager'
		verbose_name_plural = 'Managers'
	
	def __str__( self ):
		return f'{self.first_name} {self.last_name} ({self.get_department_display()})'
	@property
	def full_name( self ):
		"""Return full name"""
		return f'{self.first_name} {self.last_name}'
	@property
	def employee_count( self ):
		"""Return number of employees managed"""
		return self.employees.filter(active=True).count()
