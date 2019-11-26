from django.db import models

# Create your models here.
class CustomerContactInfo(models.Model):
    name = models.CharField(max_length=30)
    phone_no = models.CharField(max_length=15)
    operator = models.CharField(max_length=15)