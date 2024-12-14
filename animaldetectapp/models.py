from django.db import models

# Create your models here.
class Login(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    usertype=models.CharField(max_length=100)
    email=models.CharField(max_length=100)

class User(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    phone=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    street=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    pcode=models.CharField(max_length=100)
    country=models.CharField(max_length=100)
    lattitude=models.CharField(max_length=100)
    longitude=models.CharField(max_length=100)

class Animals(models.Model):
    name=models.CharField(max_length=100)
    type=models.CharField(max_length=100)
    photo=models.ImageField(upload_to='animals/')
    description=models.CharField(max_length=100)
    endangered_status=models.CharField(max_length=100)
    risk=models.CharField(max_length=100)

class ForestDivision(models.Model):
    name=models.CharField(max_length=100)
    established_year=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    area_covered=models.CharField(max_length=100)
    district=models.CharField(max_length=100)

    