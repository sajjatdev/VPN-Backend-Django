# Generated by Django 4.1.1 on 2022-09-21 14:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Loginapp', '0005_user_passcode'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='status',
        ),
    ]
