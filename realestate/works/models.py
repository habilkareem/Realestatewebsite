from django.db import models
from datetime import datetime

# Create your models here.

class Realtor(models.Model):
    username=models.CharField(max_length=30,null=True,blank=False)
    name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='images')
    description = models.TextField(blank=True)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    is_mvp = models.BooleanField(default=False)
    hire_date = models.DateTimeField(default=datetime.now, blank=True)
    password=models.CharField(max_length=30, null=False)

    def __str__(self):
        return self.name
    

class Category(models.Model):
    name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='images')

    def __str__(self):
        return self.name
    
class Listing(models.Model):
    realtor = models.ForeignKey(Realtor, on_delete=models.DO_NOTHING)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,null=True,blank=False)
    title = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=20)
    description = models.TextField(blank=True)
    price = models.IntegerField()
    bedrooms = models.IntegerField()
    bathrooms = models.DecimalField(max_digits=2, decimal_places=1)
    garage = models.IntegerField(default=0)
    sqft = models.CharField(max_length=20, blank=True)
    lot_size = models.DecimalField(max_digits=5, decimal_places=1)
    photo_main = models.ImageField(upload_to='images')
    photo_1 = models.ImageField(upload_to='images', blank=True)
    photo_2 = models.ImageField(upload_to='images', blank=True)
    photo_3 = models.ImageField(upload_to='images', blank=True)
    photo_4 = models.ImageField(upload_to='images', blank=True)
    photo_5 = models.ImageField(upload_to='images', blank=True)
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.title
    
class UserInquiry(models.Model):
    full_name = models.CharField(max_length=100)
    realtor=models.ForeignKey(Realtor,on_delete=models.CASCADE)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    message = models.TextField()

    def __str__(self):
        return self.full_name