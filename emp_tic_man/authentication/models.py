from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class CustomUser(AbstractUser):
    userRoles = (
        ('MANAGER','manager'),
        ('IT-STAFF','it staff'),
        ('EMPLOYEE','employee')
    )

    role = models.CharField(max_length=500,choices=userRoles,default='employee')
    phone = models.CharField(max_length=10)
    address = models.TextField(max_length=1000)
    email = models.CharField(max_length=300,unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','first_name','last_name','password','phone','address','role']

    def __str__(self):
        return self.username
    