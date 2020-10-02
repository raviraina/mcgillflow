from django.db import models

# Create your models here.

class Course(models.Model):
    course = models.CharField(max_length=50)
    term = models.CharField(max_length=50)
    average = models.CharField(max_length=4)
    num_average = models.CharField(max_length=4)
    num_credit = models.IntegerField()

    def __str__(self):
        return self.course + ' ' + self.term