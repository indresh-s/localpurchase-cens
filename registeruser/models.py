from django.db import models

# Create your models here.
class UserRegModel(models.Model):
	name = models.CharField(max_length=64)
	password = models.CharField(max_length=64)
	is_authenticate = models.BooleanField(default=False,null=True)