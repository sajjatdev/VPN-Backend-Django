# Generated by Django 4.1.1 on 2022-09-20 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Loginapp', '0003_user_credit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='credit',
            field=models.PositiveIntegerField(default=0),
        ),
    ]