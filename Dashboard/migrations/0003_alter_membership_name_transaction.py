# Generated by Django 4.1.1 on 2022-09-27 16:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Dashboard', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membership',
            name='name',
            field=models.CharField(choices=[('Day', 'Day'), ('Month', 'Month'), ('Years', 'Years')], default='Day', max_length=255),
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('dredit', models.PositiveIntegerField()),
                ('users', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Transaction',
                'verbose_name_plural': 'Transaction',
                'db_table': 'Transaction',
                'managed': True,
            },
        ),
    ]
