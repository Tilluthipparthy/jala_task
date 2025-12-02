from django.db import models

# Create your models here.

class Employees(models.Model):
    emp_fname = models.CharField(max_length=100)
    emp_lname = models.CharField(max_length=100)
    emp_email = models.EmailField()
    emp_number = models.BigIntegerField()  # FIXED
    emp_birth = models.DateField(default=None)
    emp_address = models.CharField(max_length=500)
    emp_country = models.CharField(max_length=100)
    emp_city = models.CharField(max_length=100)
    emp_ocity = models.CharField(max_length=100, blank=True, null=True) 
    emp_skills = models.CharField(max_length=500)

    def __str__(self):
        return self.emp_fname
    
class Image(models.Model):
    img_name=models.CharField(max_length=200)
    image = models.FileField(upload_to='uploads/', blank=True, null=True)



    def __str__(self):
        return self.img_name


