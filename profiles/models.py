from django.db import models
from django.contrib.auth.models import User
#from PIL import Image

# Create your models here.
class Student(models.Model):
    #user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    #user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True)
    name = models.CharField(max_length=150)
    #models.ForeignKey(User, on_delete=models.CASCADE)
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
        return self.name

class Club(models.Model):
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=350, default="a club on Grounds")
    members = models.ManyToManyField(
        Student,
        through="Membership",
        through_fields=('club', 'student')
    )

    def __str__(self):
        return self.name

class Course(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=350, default="a course on Grounds")
    long_description = models.TextField(
        default="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer pulvinar ipsum mattis laoreet dictum. Donec et odio ligula. Nullam et purus quam. Duis vel malesuada purus, at iaculis est. Donec eget placerat augue. Sed pharetra pellentesque augue at ultrices. Cras ac massa eleifend, blandit ligula sed, porttitor magna. Etiam massa eros, sollicitudin eu sem eget, bibendum ultrices turpis. Mauris tincidunt convallis ligula vel vehicula. Aliquam in leo vel justo rutrum tempus a fringilla ante. Proin rhoncus commodo dui, sed volutpat lorem gravida vel. Sed non lacus viverra, ultrices purus id, maximus nunc. Mauris vitae urna diam. Donec quis posuere enim. Cras a nibh porttitor, tincidunt enim nec, rhoncus nibh.")
    '''
    COURSE_LIST = [
    ("CS1110",1),
    ("CS2110",2),
    ("CS2150",3),
    ("CS3102",4),
    ("CS3330",5),
    ("CS4102",6),
    ("CS4414",7),
    ("CS4740",8),
    ("CS4720",9),
    ]'''

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('title',)

class Membership(models.Model):
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    courses = models.ManyToManyField(Course)
#    image = models.ImageField(default='default.jpg', upload_to='profile_pics')


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


def save(self, force_insert=False, force_update=False, using=None):
        super().save()


'''
        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
'''
