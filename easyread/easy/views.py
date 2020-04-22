from django.shortcuts import render,redirect, reverse
from django.http import HttpResponse
from . import utils as util
from . import forms
from .models import Document
from django.db import transaction

try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

# Create your views here.
def index(request):
	if request.method == 'POST':
		form = forms.UploadPost(request.POST, request.FILES)
		if form.is_valid():
			instance = form.save()
			timetable = instance.photo
			kulliya = instance.kulliya
			image = Image.open(timetable)
			filename = "output{0}".format(instance.id)
			text = pytesseract.image_to_string(image).upper()
			file = open("media/raw/%s"%filename,"w")
			file.write(text)
			file.close()
			instance.output_file = "raw/"+filename
			instance.save()
			# query = util.queries(lines, kulliya)
			# return render(request,'easy/index.html',{'queries':query} )
			return redirect("home:schedule", id=instance.unique_id)
	else:
		form = forms.UploadPost()
	return render(request, 'easy/upload.html', {'form': form})

def timetable(request, id):
	document = Document.objects.get(unique_id=id)
	with open(document.output_file.path) as f:
		lines = f.readlines()
	document.converted_text = lines
	document.save()
	query = util.queries(lines, document.kulliya)
	# return HttpResponse(document.kulliya)
	return render(request, 'easy/index.html', {'queries':query})
