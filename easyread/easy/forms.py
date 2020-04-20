from django import forms
from . import models

class UploadPost(forms.ModelForm):
	class Meta:
		model = models.Post
		fields = ['year','photo']