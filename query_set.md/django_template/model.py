from django.db import models

#using abstract class
class commonInfo(models.Model):
          name=models.CharField(max_length=100)
          age =models.PositiveIntegerField()

          class Meta:
                    abstract =True

class Student(commonInfo):
          home_group =models.CharField(max_length=5)
          #now this table has name,age 


#one to one relationship
class Place(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=80)
    

class Restaurant(Place):
    serves_hot_dogs = models.BooleanField(default=False)
    serves_pizza = models.BooleanField(default=False)
    class Meta:
          proxy =True #we can access the by resturant

