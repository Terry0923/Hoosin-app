# Generated by Django 2.1.7 on 2019-02-17 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('year', models.CharField(choices=[('FIRST', 1), ('SECOND', 2), ('THIRD', 3), ('FOURTH', 4)], default='FIRST', max_length=6)),
            ],
        ),
    ]
