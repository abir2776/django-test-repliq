from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Company(models.Model):
    title = models.CharField(max_length=50)
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='user')
    location = models.CharField(max_length=20)
    mobile = models.CharField(max_length=15)

    def __str__(self):
        return self.title
    
class Employee(models.Model):
    name = models.CharField(max_length=20)
    company = models.ForeignKey(Company,on_delete=models.CASCADE,related_name="company")
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.name
    
class Device(models.Model):
    class Type(models.TextChoices):
        pending = 'phone', _('Phone')
        rejected = 'tablet', _('Tablet')
        request_change = 'laptop', _('Laptop')
    brand = models.CharField(max_length=20)
    type = models.CharField(max_length=10, choices=Type.choices)
    employee = models.ForeignKey(Employee,on_delete=models.CASCADE,related_name='employee')
    check_out = models.DateTimeField(auto_now_add=True)
    returned = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.type

