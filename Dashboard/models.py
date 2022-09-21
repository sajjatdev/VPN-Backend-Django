from uuid import uuid1
from django.db import models

# Create your models here.


class update(models.Model):
    id = models.UUIDField(unique=True, primary_key=True,
                          default=uuid1, editable=False, max_length=20)
    name = models.CharField(max_length=255)
    jsondata = models.TextField()

    status = models.BooleanField(default=True)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'update'
        managed = True
        verbose_name = 'update'
        verbose_name_plural = 'updates'