from django.db import models
from django.contrib.postgres.fields import JSONField
from django.contrib.auth.models import User

YEAR = (
    ('year1','YEAR 1'),
    ('year2','YEAR 2'),
    ('year3','YEAR 3'),
    ('year4','YEAR 4'),
)

class Post(models.Model):
	title = models.CharField(max_length=100)
	year = models.CharField(max_length=20, choices=YEAR, default="Year1")
	photo = models.ImageField()

	def __str__(self):
		return self.title

class Course(models.Model):
	course_code = models.CharField(max_length=15)
	course_name = models.CharField(max_length=100)
	credit_hour = models.FloatField()
	# year = models.ManyToManyField(YEAR, blank=True, related_name='year')

	def __str__(self):
		return "{0} {1}".format(self.course_code, self.course_name)

class Student(models.Model):
	name = models.CharField(max_length=200)
	data = JSONField()

	def __str__(self):
		return self.name