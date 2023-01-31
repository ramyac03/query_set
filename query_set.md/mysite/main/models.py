from django.db import models
from datetime import date
# Create your models here.
class Define(models.Model):
         name =models.CharField(max_length=200,verbose_name="first name")
         def __str__(self):
                 return self.name

class Info(models.Model):
         define =models.ForeignKey(Define,on_delete=models.CASCADE)
         #define =models.ManyToManyFields(Define) -->many to many relationship

         email =models.CharField(max_length=100)
         def __str__(self):
                 return self.email


#using abstract class
class commonInfo(models.Model):
          name=models.CharField(max_length=100)
          age =models.PositiveIntegerField()

          class Meta:
                    abstract =True

class Student(commonInfo):
          home_group =models.CharField(max_length=5)
          #now this table has name,age 

class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()

    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Entry(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    headline = models.CharField(max_length=255)
    body_text = models.TextField()
    pub_date = models.DateField()
    mod_date = models.DateField(default=date.today)
    authors = models.ManyToManyField(Author)
    number_of_comments = models.IntegerField(default=0)
    number_of_pingbacks = models.IntegerField(default=0)
    rating = models.IntegerField(default=5)

    def __str__(self):
        return self.headline