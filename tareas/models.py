from django.db import models

# Create your models here.
class Task(models.Model):
	titulo = models.CharField(max_length=200)
	descripcion = models.CharField(max_length=200)
	hecha = models.BooleanField(default=False)