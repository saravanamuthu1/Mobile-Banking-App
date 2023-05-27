from django.db import models

# Create your models here.

class apidata(models.Model):
    code=models.CharField(max_length=5,null=True,unique=True)
    value=models.FloatField(max_length=20,unique=True)

class money(models.Model):
    balance=models.IntegerField()

class accountactivity(models.Model):
    sender_mail=models.EmailField(max_length=100)
    amount=models.IntegerField()
    datafield=models.DateField(null=True)
    timefield=models.TimeField(null=True)

class splitbill(models.Model):
    email=models.EmailField(max_length=50)