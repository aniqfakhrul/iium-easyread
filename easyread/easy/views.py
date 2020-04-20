from django.shortcuts import render,redirect, reverse
from django.http import HttpResponse
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
			file = open("text_file","w")
			file.write(text)
			file.close()
			# return redirect(reverse('home:schedule', kwargs={'classname': instance.title}))
			return redirect('home:schedule')
			# return render(request,'easy/index.html',{'queries':query} )
	else:
		form = forms.UploadPost()
	return render(request, 'easy/upload.html', {'form': form})

def timetable(request):
	with open("text_file") as f:
		text = f.readlines()
	# head = text.index("COURSE SEC STA TITLE CHR DAY TIME VENUE\n")
	# tail = text.index("ANNOUNCEMENT FROM ACADEMIC MANAGEMENT AND ADMISSION DIVISION\n")
	lines = text
	query = util.queries(lines)
	# return HttpResponse(query)
	return render(request, 'easy/index.html', {'queries':query})
