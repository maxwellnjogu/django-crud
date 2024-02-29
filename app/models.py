from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=25,blank=False,null=False)
    email=models.EmailField()
    age=models.IntegerField()
    gender=models.CharField(max_length=25,blank=False,null=False)
    image = models.ImageField(upload_to='uploads/images', default="logo.png")

    def __str__(self) :
        return self.name
