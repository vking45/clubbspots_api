from django.db import models
from django.conf import settings
from django.urls import reverse

# Create your models here.
class Club(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    maxcap = models.IntegerField()
    currcap = models.IntegerField()
    waitcap = models.IntegerField()
    updatedtime = models.DateTimeField(auto_now= True)
    image1 = models.URLField(blank=True)
    image2 = models.URLField(blank=True)
    image3 = models.URLField(blank=True)

    def __str__(self):
      return self.name
    def get_absolute_url(self):
        return reverse('updateclient', kwargs={"pk": self.pk})
    
   
  
              
class Media(models.Model):
    name = models.CharField(max_length=100) 
    images1 = models.ImageField(upload_to='clients/images', default="")
    images2 = models.ImageField(upload_to='clients/images', default="")
    images3 = models.ImageField(upload_to='clients/images', default="")

    def __str__(self):
      return self.name

class Report(models.Model):
    venture = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    issue = models.TextField()

    def __str__(self):
        return self.venture