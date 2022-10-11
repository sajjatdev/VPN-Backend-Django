from uuid import uuid1
from django.db import models
from datetime import datetime
from django.conf import settings


class Payload(models.Model):
    name = models.CharField(max_length=255)
    payload = models.TextField(max_length=500)
    SSL = models.CharField(max_length=255, default="none")
    proxyIP = models.CharField(max_length=255)
    proxyport = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Payload'
        managed = True
        verbose_name = 'Payload'
        verbose_name_plural = 'Payload'


class Server(models.Model):
    name = models.CharField(max_length=255)
    Flag = models.ImageField(upload_to='flag/')
    Server_Host = models.CharField(max_length=255)
    Server_Port = models.CharField(max_length=255)
    SSL_Port = models.CharField(max_length=255)
    UDP_port = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Server'
        managed = True
        verbose_name = 'Server'
        verbose_name_plural = 'Servers'


class ServerJson(models.Model):
    id = models.UUIDField(unique=True, primary_key=True,
                          default=uuid1, editable=False, max_length=20)
    name = models.CharField(max_length=255)
    server = models.ManyToManyField(Server)
    payload = models.ManyToManyField(Payload)
    status = models.BooleanField(default=True)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'ServerJson'
        managed = True
        verbose_name = 'ServerJson'
        verbose_name_plural = 'ServerJsons'


class Membership(models.Model):
    name = [("Day", "Day"),
            ("Month", "Month"), ("Years", "Years")]
    title = models.CharField(max_length=255)
    duration = models.PositiveIntegerField()
    name = models.CharField(
        choices=name, default="Day", max_length=255)

    def __str__(self):
        return str(self.duration) + " " + self.name

    class Meta:
        db_table = 'membership'


class Customer(models.Model):
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=6,)
    is_active = models.BooleanField(default=True)
    join_date = models.DateTimeField(auto_now_add=True)
    expire_date = models.DateTimeField(default=datetime.now)
    membership = models.ForeignKey(Membership, on_delete=models.CASCADE)
    reseller = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Customer'
        managed = True
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'


class Transaction(models.Model):
    users = models.ForeignKey(settings.AUTH_USER_MODEL,
                              on_delete=models.CASCADE, related_name='users')
    create_at = models.DateTimeField(auto_now_add=True)
    authors = models.ForeignKey(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE, related_name='authors')
    balance = models.PositiveIntegerField()

    class Meta:
        db_table = 'Transaction'
        managed = True
        verbose_name = 'Transaction'
        verbose_name_plural = 'Transaction'
