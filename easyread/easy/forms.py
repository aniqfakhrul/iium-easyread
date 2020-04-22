from django import forms
from . import models

class UploadPost(forms.ModelForm):
	class Meta:
		model = models.Document
		fields = ['kulliya','photo']