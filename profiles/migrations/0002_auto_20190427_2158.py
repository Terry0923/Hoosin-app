# Generated by Django 2.1.5 on 2019-04-28 02:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='description',
            field=models.CharField(default='a course on Grounds', max_length=4000),
        ),
    ]
