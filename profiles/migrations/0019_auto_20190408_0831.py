# Generated by Django 2.1.5 on 2019-04-08 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0018_auto_20190405_2017'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='description',
            field=models.CharField(default='a course on Grounds', max_length=350),
        ),
        migrations.AddField(
            model_name='course',
            name='long_description',
            field=models.TextField(default='Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer pulvinar ipsum mattis laoreet dictum. Donec et odio ligula. Nullam et purus quam. Duis vel malesuada purus, at iaculis est. Donec eget placerat augue. Sed pharetra pellentesque augue at ultrices. Cras ac massa eleifend, blandit ligula sed, porttitor magna. Etiam massa eros, sollicitudin eu sem eget, bibendum ultrices turpis. Mauris tincidunt convallis ligula vel vehicula. Aliquam in leo vel justo rutrum tempus a fringilla ante. Proin rhoncus commodo dui, sed volutpat lorem gravida vel. Sed non lacus viverra, ultrices purus id, maximus nunc. Mauris vitae urna diam. Donec quis posuere enim. Cras a nibh porttitor, tincidunt enim nec, rhoncus nibh.'),
        ),
    ]
