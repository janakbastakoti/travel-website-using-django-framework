from django.db import models

# Create your models here.
class Destination(models.Model):
    name        = models.CharField(max_length=30)
    img         = models.ImageField(upload_to='pics')
    discription = models.TextField()
    price       = models.IntegerField()
    offer       = models.BooleanField(default=False)


class Experience(models.Model):
    name        = models.CharField(max_length=30)
    img         = models.ImageField(upload_to='pics')
    discription = models.TextField()
    designation = models.CharField(default=None,max_length=40)

class Blog(models.Model):
    name        = models.CharField(max_length=30)
    topic       = models.CharField(max_length=100)
    img         = models.ImageField(default=False ,upload_to='pics')
    discription = models.TextField()
    date        = models.IntegerField()
    
    
