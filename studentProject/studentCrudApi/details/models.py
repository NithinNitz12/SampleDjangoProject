from django.db import models

# Create your models here.
class Students(models.Model):
    Name = models.CharField(max_length=100,blank=True)
    Age = models.CharField(max_length=100, blank=True)
    Address = models.CharField(max_length=100, blank=True)
    Email = models.CharField(max_length=100, blank=True)
    Mob_no = models.CharField(max_length=100, blank=True)
    City = models.CharField(max_length=100, blank=True)
    Current_Designation = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.Name