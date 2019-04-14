# Generated by Django 2.1.5 on 2019-04-14 22:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Club',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('description', models.CharField(default='a club on Grounds', max_length=350)),
                ('image', models.ImageField(default='default.jpg', upload_to='club_pics')),
                ('users', models.ManyToManyField(default=[], to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField(default='here is some comment body text', max_length=1000)),
                ('date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('description', models.CharField(default='a course on Grounds', max_length=350)),
                ('long_description', models.TextField(default='Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer pulvinar ipsum mattis laoreet dictum. Donec et odio ligula. Nullam et purus quam. Duis vel malesuada purus, at iaculis est. Donec eget placerat augue. Sed pharetra pellentesque augue at ultrices. Cras ac massa eleifend, blandit ligula sed, porttitor magna. Etiam massa eros, sollicitudin eu sem eget, bibendum ultrices turpis. Mauris tincidunt convallis ligula vel vehicula. Aliquam in leo vel justo rutrum tempus a fringilla ante. Proin rhoncus commodo dui, sed volutpat lorem gravida vel. Sed non lacus viverra, ultrices purus id, maximus nunc. Mauris vitae urna diam. Donec quis posuere enim. Cras a nibh porttitor, tincidunt enim nec, rhoncus nibh.')),
            ],
            options={
                'ordering': ('title',),
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.CharField(max_length=250)),
                ('body', models.TextField(default='here is some post body text')),
                ('image', models.ImageField(default='default.jpg', upload_to='profile_pics')),
                ('type', models.CharField(choices=[('event', 'event'), ('announcement', 'announcement'), ('misc', 'misc')], default='announcement', max_length=12)),
                ('date', models.DateTimeField()),
                ('club', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='profiles.Club')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='default.jpg', upload_to='profile_pics')),
                ('status', models.CharField(choices=[('looking for a study buddy', 'looking for a study buddy'), ('looking for a study group', 'looking for a study group'), ('looking for a tutor', 'looking for a tutor'), ('available to tutor', 'available to tutor')], default='looking for a study buddy', max_length=50)),
                ('bio', models.TextField(default='some information about the student')),
                ('year', models.CharField(choices=[('first', 1), ('second', 2), ('third', 3), ('fourth', 4)], default='first', max_length=6)),
                ('major', models.CharField(default='undeclared', max_length=150)),
                ('friends', models.ManyToManyField(related_name='Friend', to=settings.AUTH_USER_MODEL)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('year', models.CharField(choices=[('first', 1), ('second', 2), ('third', 3), ('fourth', 4)], default='first', max_length=6)),
                ('major', models.CharField(default='undeclared', max_length=150)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='profile',
            field=models.ManyToManyField(default=[], to='profiles.Profile'),
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='profiles.Post'),
        ),
        migrations.AddField(
            model_name='comment',
            name='profile',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='profiles.Profile'),
        ),
    ]
