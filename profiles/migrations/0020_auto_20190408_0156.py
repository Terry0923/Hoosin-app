# Generated by Django 2.1.5 on 2019-04-08 05:56

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('profiles', '0019_auto_20190407_2356'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='club',
            name='profiles',
        ),
        migrations.AddField(
            model_name='club',
            name='users',
            field=models.ManyToManyField(default=[], to=settings.AUTH_USER_MODEL),
        ),
    ]
