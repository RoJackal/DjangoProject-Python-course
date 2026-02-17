from django.db import models

from manager.models import Manager

gender_options = [
    ('male', 'Male'),  # ('cea salvata in DB', 'cea afisata in interfata')
    ('female', 'Female'),
    ]
class Employee(models.Model):
    first_name = models.CharField(max_length=30)  # max_length este de 255 de caractere
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=50, null=True, blank=True)
    age = models.PositiveIntegerField()  # sau IntegerField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    gender = models.CharField(choices=gender_options, max_length=6)
    hire_date = models.DateField()
    active = models.BooleanField(default=True)
    manager = models.ForeignKey(Manager, on_delete=models.CASCADE, null=True, blank=True)
    # campuri auxiliare
    created_at = models.DateTimeField(auto_now_add=True)  # voi stoca data si ora in momentul in care angajatul a fost salvat cu succes
    updated_at = models.DateTimeField(auto_now=True)  # voi stoca data si ora atunci cand se realizeaza ultima modificare per angajat
    def __str__( self ):
        return f'{self.first_name} {self.last_name}'
