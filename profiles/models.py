from django.db import models
from django.contrib.auth.models import User
#from PIL import Image


# foundation for Profile object
class Student(models.Model):
    #user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=150)
    YEAR_CHOICES = [("first", 1),
                    ("second", 2),
                    ("third", 3 ),
                    ("fourth", 4)]
    year = models.CharField(
        max_length=6,
        choices=YEAR_CHOICES,
        default="first")
    major = models.CharField(max_length=150, default="undeclared")

    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    bio = models.TextField(default="some information about the student")

    YEAR_CHOICES = [("first", 1),
                    ("second", 2),
                    ("third", 3 ),
                    ("fourth", 4)]
    year = models.CharField(
        max_length=6,
        choices=YEAR_CHOICES,
        default="first")
    major = models.CharField(max_length=150, default="undeclared")

    def __str__(self):
        return f'{self.user.username} Profile'



class Club(models.Model):
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=350, default="a club on Grounds")
    image = models.ImageField(default='default.jpg', upload_to='club_pics')
    users = models.ManyToManyField(User, default=[])
    def __str__(self):
        return self.name


class Post(models.Model):
    headline = models.CharField(max_length=250)
    body = models.TextField(default="here is some post body text")
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    profile = models.ManyToManyField(Profile, default=[])

    TYPE_CHOICES = [("event", "event"),
                    ("announcement", "announcement"),
                    ("misc", "misc")]
    type = models.CharField(
        max_length=12,
        choices=TYPE_CHOICES,
        default="announcement")
    date = models.DateTimeField()
    club = models.ForeignKey(Club, default=None, on_delete=models.CASCADE)


def save(self, force_insert=False, force_update=False, using=None):
        super().save()


'''
        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
'''
