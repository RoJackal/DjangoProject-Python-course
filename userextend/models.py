from django.db import models

# Create your models here.

class Logs(models.Model):
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text