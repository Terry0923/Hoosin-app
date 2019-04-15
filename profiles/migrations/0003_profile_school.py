# Generated by Django 2.1.7 on 2019-04-15 02:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_profile_friends'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='school',
            field=models.CharField(choices=[('School of Nursing', 'School of Nursing'), ('School of Medicine', 'School of Medicine'), ('School of Law', 'School of Law'), ('School of Engineering and Applied Science', 'School of Engineering and Applied Science'), ('Curry School of Education and Human Development', 'Curry School of Education and Human Development'), ('Darden School of Business', 'Darden School of Business'), ('Mcintire School of Commerce', 'Mcintire School of Commerce'), ('School of Architecture', 'School of Architecture')], default='School of Engineering and Applied Science', max_length=50),
        ),
    ]
