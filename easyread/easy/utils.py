from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
import re
from .models import Course, Student
from datetime import *

query = {}
courses =	{
  "CCSB 3211": "SWIMMING SKILLS 1 (BROTHER)",
  "INFO 3102": "DATA WAREHOUSING",
  "INFO 3305": "WEB APPLICATION DEVELOPMENT",
  "INFO 3501": "PROJECT MANAGEMENT INIT",
  "LE 4000": "ENGLISH FOR ACADEMIC WRITING (EAW)",
  "MPU 3I12": "HUBUNGAN ETNIK",
  "UNGS 2011": "CREATIVE THINKING AND PROBLEM",
}

days = {
	"MON" : ['Monday'],
	"MW" : ['Monday', 'Wednesday'],
	"TUE" : ["Tuesday"],
	"AH" : ["Tuesday", "Thursday"],
	"WED" : ["Wednesday"],
	"THUR" : ["Thursday"],
	"FRI" : ["Friday"],
}

time = {
	"500-7" : ['5:00 PM','7:00 PM'],
	"830 -950" : ['8:30 AM','9:50 AM'],
	"330 -450" : ['3:30 PM','4:50 PM'],
	"1030-1220" : ['10:30 AM','12:20 PM'],
	"10.00 «11.20" : ['10:00 AM','11:20 AM'],
	"200 -320" : ['2:00 PM','3:20 PM'],
	"1030-1220" : ['10:30 AM','12:20 PM'],
	"1.50" : ['12:00 PM','1:50 PM'],
}

timeunit = ['AM', 'PM']

all_course = []
course = {
	"code" : "",
	"name" : "",
	"day" : [],
	"time" : "",
	"venue" : "",
}

def queries(lines):
	for line in lines:
		#get class venue
		if re.findall('\\b AM\\b', line):
			course.update({"venue" : line[line.find(' AM')+3:].lstrip()})
		elif re.findall('\\b PM\\b', line):
			course.update({"venue" : line[line.find(' PM')+3:].lstrip().strip("\n")})

		#get couse code and name
		posts = Course.objects.all()
		for post in posts:
			if (post.course_code in line) or (post.course_code.replace(" ","") in line): #check available course code
				course.update({"code" : post.course_code.replace(" ","")})
				course.update({"name" : post.course_name})
				break

		#get class day
		for k, v in days.items():
			if k in line:
				course.update({"day":v})
				break

		#get class time
		for k, v in time.items():
			if k in line:
				# course.update({"time":v})
				v[0] = datetime.strptime(v[0], '%I:%M %p')
				v[0] = datetime.strftime(v[0], "%H:%M")
				v[1] = datetime.strptime(v[1], '%I:%M %p')
				v[1] = datetime.strftime(v[1], "%H:%M")
				innerDict = {"start":str(v[0]), "end":str(v[1])}
				course["time"]=innerDict
				all_course.append(course.copy())
				# Student.objects.create(name='Aniqq', data={course})
				break
	return all_course