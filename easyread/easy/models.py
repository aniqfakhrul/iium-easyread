from django.db import models
from django.contrib.postgres.fields import JSONField
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField

KULLIYA = (
    ('AHS','ALLIED HEALTH SCIENCES'),
    ('HS','HUMAN SCIENCES'),
    ('KAED','ARCHITECTURE'),
    ('CELPAD','CELPAD'),
    ('COCU','COCU'),
    ('DENTISTRY','DENTISTRY'),
    ('EDUCATION','EDUCATION'),
    ('ENGIN','ENGIN'),
    ('ENMS','ENMS'),
    ('KICT','KICT'),
    ('IRKHS','IRKHS'),
    ('ISLAMICBF','ISLAMIC BANKING AND FINANCE'),
    ('ISTAC','ISTAC'),
    ('KLM','KLM'),
    ('LAWS','LAWS'),
    ('MEDICINE','MEDICINE'),
    ('NURSING','NURSING'),
    ('PHARMACY','PHARMACY'),
    ('SCIENCE','SCIENCE'),
)

class Document(models.Model):
	# title = models.CharField(max_length=100)
	unique_id = models.CharField(max_length=11,editable=False, unique=True, null=True)
	kulliya = models.CharField(max_length=20, choices=KULLIYA, default="ALLIED HEALTH SCIENCES")
	photo = models.ImageField()
	output_file = models.FileField(default="output")
	uploaded_at = models.DateTimeField(auto_now_add=True)
	converted_text = models.TextField(blank=True)

	def __str__(self):
		return str(self.id)

	def save(self):
		# head, sed, file_name = (self.photo.name).partition("_")
		# self.unique_id = file_name[:-4]
		# super(Document, self).save()
		if not self.unique_id:
			# Generate ID once, then check the database. If exists, keep trying.
			self.unique_id = generate_random_string()
			while Document.objects.filter(unique_id=self.unique_id).exists():
				self.unique_id = generate_random_string()
		super(Document, self).save()


class Course(models.Model):
	course_code = models.CharField(max_length=15)
	course_name = models.CharField(max_length=100)
	credit_hour = models.FloatField()
	kulliya = models.CharField(max_length=20, choices=KULLIYA, default="ALLIED HEALTH SCIENCES")
	uni_required = models.BooleanField(default=False)

	class Meta:
		unique_together = ["course_code"]

	def __str__(self):
		return "{0} | {1} [{2}]".format(self.course_code, self.course_name, self.kulliya)

	def save(self):
	       self.course_name = self.course_name.title()
	       super(Course, self).save()

class Time(models.Model):
	time_input = models.CharField(max_length=15)
	time_output = ArrayField(models.CharField(max_length=10, blank=True), size=2)

	class Meta:
		unique_together = ["time_input"]

	def __str__(self):
		return "{0}".format(self.time_input)

	def save(self):
	       self.course_name = self.course_name.title()
	       super(Course, self).save()


import string
import random

LENGTH = 11


def generate_random_string():
    """
    Generates random ID.
    """
    random_string = string.digits + string.ascii_uppercase
    new_id = ''.join([random.SystemRandom().choice(random_string) for i in range(random.randint(11, LENGTH))])
    return new_id