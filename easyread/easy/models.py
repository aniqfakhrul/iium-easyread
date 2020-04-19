from django.db import models
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