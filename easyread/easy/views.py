from django.shortcuts import render,redirect, reverse
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import utils as util
from . import forms

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
			instance = form.save(commit=False)
			timetable = instance.photo
			image = Image.open(timetable)
			text = pytesseract.image_to_string(image).upper()
			file = open("text_file","r+")
			file.write(text)
			file.close()
			with open("text_file") as f:
				text = f.readlines()
			head = text.index("COURSE SEC STA TITLE CHR DAY TIME VENUE\n")
			tail = text.index("ANNOUNCEMENT FROM ACADEMIC MANAGEMENT AND ADMISSION DIVISION\n")
			lines = text[head:tail]
			query = util.queries(lines)
			# return redirect(reverse('home:schedule', kwargs={'classname': instance.title}))
			# return HttpResponse(util.all_course)
			return render(request,'easy/index.html',{"all_course":util.all_course} )
	else:
		form = forms.UploadPost()
	return render(request, 'easy/upload.html', {'form': form})

@login_required(login_url='/')
def timetable(request):
	return render(request, 'easy/index.html')
