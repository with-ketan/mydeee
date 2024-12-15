from django.db import models

# Create your models here.
class AboutMe(models.Model):
    Name=models.CharField(max_length=250)
    Eduction=models.CharField(max_length=230)
    Email=models.EmailField()
    Phone=models.IntegerField()
    Address=models.CharField(max_length=130)

    def __str__(self):
        return self.Name
    
class Contact(models.Model):
    name=models.CharField(max_length=25)
    email=models.EmailField()
    phonenumber=models.CharField(max_length=10,default="phone")
    description=models.TextField()

    def __str__(self):
        return self.name
    
class Service(models.Model):
    name = models.CharField(max_length=100, verbose_name="Service name")
    description = models.TextField(verbose_name="About service")

    def __str__(self):
        return self.name
    
