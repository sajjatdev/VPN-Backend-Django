# Generated by Django 4.1.1 on 2022-09-20 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Loginapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='createby',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]