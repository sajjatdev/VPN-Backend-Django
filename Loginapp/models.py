
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):

    email = models.EmailField(unique=True)
    create_at = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    createby = models.CharField(max_length=255)
    credit = models.PositiveIntegerField(default=0)
    passcode = models.CharField(max_length=255)

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'user'
        managed = True
        verbose_name = 'User'
        verbose_name_plural = 'Users'
