from django.db import models
from tinymce.models import HTMLField
from versatileimagefield.fields import VersatileImageField

# Create your models here.
class HomeBanner(models.Model):
    title = models.CharField(max_length=100)
    description = HTMLField()
    def __str__(self):
        return self.title

class Service(models.Model):
    catagory = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    description = HTMLField()
    image = VersatileImageField(upload_to = "service")
    def __str__(self):
        return self.title


class Works(models.Model):
    catagory = models.CharField(max_length=100)
    image = VersatileImageField(upload_to = "works")
    title = models.CharField(max_length=100)
    client = models.CharField(max_length=100)
    date = models.DateField()
    link = models.URLField(blank=True, null=True)
    description = HTMLField()
    def __str__(self):
        return self.title
    
class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    image = VersatileImageField(upload_to = "testimonial")
    description = HTMLField()
    def __str__(self):
        return self.name

class Blog(models.Model):
    title = models.CharField(max_length=200)
    description = HTMLField()
    image = VersatileImageField(upload_to = "blog")
    date = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.title
    
class Journey(models.Model):
    title = models.CharField(max_length=100)
    description = HTMLField()
    image = VersatileImageField(upload_to = "journey")
    def __str__(self):
        return self.title
    

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = HTMLField()

    def __str__(self):
        return self.name