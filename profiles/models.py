from django.db import models


# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=150)
    YEAR_CHOICES = [("FIRST",1),
                    ("SECOND", 2),
                    ("THIRD", 3),
                    ("FOURTH", 4)]
    year = models.CharField(
        max_length=6,
        choices=YEAR_CHOICES,
        default="FIRST")

    def __str__(self):
        return self.name


class Club(models.Model):
    name = models.CharField(max_length=150)
    members = models.ManyToManyField(
        Student,
        through="Membership",
        through_fields=('club', 'student')
    )

    def __str__(self):
        return self.name

class Membership(models.Model):
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
