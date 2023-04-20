from django.db import models

# Create your models here.

class apidata(models.Model):
    code=models.CharField(max_length=5,null=True,unique=True)
    value=models.FloatField(max_length=20,unique=True)

class money(models.Model):
    balance=models.IntegerField()
