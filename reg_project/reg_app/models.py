
from django.db import models


# Create your models here.


class Register(models.Model):
    # id = models.IntegerField
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phonenumber = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    confirmpassword = models.CharField(max_length=100)
    # alternatephoneNumber = models.CharField(max_length=100,default=True)
    # addressline1 = models.CharField(max_length=100,default=True)
    # addressline2 = models.CharField(max_length=100,default=True)
    # countryorcity = models.CharField(max_length=100,default=True)
    # postalcode = models.CharField(max_length=100,default=True)
    # companyname = models.CharField(max_length=100,default=True)
    # companytype = models.CharField(max_length=100,default=True)    
    # addressline1 = models.CharField(max_length=100,default=True)
    # addressline2 = models.CharField(max_length=100,default=True)
    # countryorcity = models.CharField(max_length=100,default=True)
    # postalcode = models.CharField(max_length=100,default=True)

    # objects = UserManager()

    # USERNAME_FIELD = 'firstname'
    # REQUIRED_FIELD = []

    # class meta:
    #     db_table = 'Register'

   
