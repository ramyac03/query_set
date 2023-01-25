from django.db import models

# Create your models here.
class Define(models.Model):
         name =models.CharField(max_length=200)
         def __str__(self):
                 return self.name

class Info(models.Model):
         define =models.ForeignKey(Define,on_delete=models.CASCADE)
         email =models.CharField(max_length=100)
         def __str__(self):
                 return self.email


