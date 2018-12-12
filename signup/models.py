from django.db import models


# Create your models here.
class Account(models.Model):
    username = models.CharField(max_length=30, unique=True)
    first_name = models.CharField('first name', max_length=30)
    last_name = models.CharField('last name', max_length=30)
    email = models.EmailField('e-mail address')
    password = models.CharField('password', max_length=128)

    def __str__(self):
        return self.username
