# Generated by Django 2.1.7 on 2019-02-22 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_auto_20190222_0143'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='major',
            field=models.CharField(default='undeclared', max_length=150),
        ),
        migrations.AlterField(
            model_name='student',
            name='year',
            field=models.CharField(choices=[('first', 1), ('second', 2), ('third', 3), ('fourth', 4)], default='first', max_length=6),
        ),
    ]
