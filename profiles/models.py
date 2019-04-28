from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
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
    STATUS_CHOICES = [("looking for a study buddy", "looking for a study buddy"),
                      ("looking for a study group", "looking for a study group"),
                      ("looking for a tutor", "looking for a tutor"),
                      ("available to tutor", "available to tutor")]
    status = models.CharField(
        max_length=50,
        choices=STATUS_CHOICES,
        default="looking for a study buddy")
    friends = models.ManyToManyField(User, related_name="Friend")
    SCHOOL_CHOICES = [
    ("School of Nursing","School of Nursing"),
    ("College of Arts and Sciences", "College of Arts and Sciences"),
    ("School of Medicine","School of Medicine"),
    ("School of Law","School of Law"),
    ("School of Engineering and Applied Science","School of Engineering and Applied Science"),
    ("Curry School of Education and Human Development","Curry School of Education and Human Development"),
    ("Darden School of Business","Darden School of Business"),
    ("Mcintire School of Commerce","Mcintire School of Commerce"),
    ("School of Architecture","School of Architecture"),
    ]
    school = models.CharField(
        max_length=50,
        choices=SCHOOL_CHOICES,
        default ="School of Engineering and Applied Science")
    YEAR_CHOICES = [("first", 1),
                    ("second", 2),
                    ("third", 3),
                    ("fourth", 4)]
    year = models.CharField(
        max_length=6,
        choices=YEAR_CHOICES,
        default="first")
    major = models.CharField(max_length=150, default="undeclared")

    def __str__(self):
        return f'{self.user.username} Profile'


class Course(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=4000, default="a course on Grounds")
    long_description = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('title',)


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


class Comment(models.Model):
    body = models.TextField(default="here is some comment body text", max_length=1000)
    profile = models.ForeignKey(Profile, default=None, on_delete=models.CASCADE)
    # each comment has only one profile that posted it, but profiles can make multiple comments
    post = models.ForeignKey(Post, default=None, on_delete=models.CASCADE)
    # each comment has only one post it's associated with, but posts can have multiple comments
    date = models.DateTimeField()


def save(self, force_insert=False, force_update=False, using=None):
        super().save()


'''
        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
'''
