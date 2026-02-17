from django.db import models


class Manager(models.Model):

    department_options = [
        ('hr', 'Human Resources'),
        ('it', 'Information Technology'),
        ('sales', 'Sales'),
        ('marketing', 'Marketing'),
        ('finance', 'Finance'),
    ]

    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    email = models.EmailField(max_length=60, unique=True)
    department = models.CharField(max_length=20, choices=department_options)
    hire_date = models.DateField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
