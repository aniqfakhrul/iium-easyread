from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
import re

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
	"AH" : ["Tuesday", "Thursay"],
	"WED" : ["Wednesday"],
	"THUR" : ["Thursday"],
	"FRI" : ["Friday"],
}

time = {
	"500-7" : ['5:00','7:00'],
	"830 -950" : ['8:30','9:50'],
	"330 -450" : ['3:30','4:50'],
	"1030-1220" : ['10:30','12:20'],
	"10.00 «11.20" : ['10:00','11:20'],
	"200 -320" : ['2:00','3:20'],
	"1030-1220" : ['10:30','12:20'],
	"1.50" : ['12:00','1:50'],
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
			course.update({"venue" : line[line.find(' PM')+3:].lstrip()})

		#get couse code and name
		for course_id, course_name in courses.items():
			if (course_id in line) or (course_id.replace(" ","") in line): #check available course code
				course.update({"code" : course_id.replace(" ","")})
				course.update({"name" : course_name})
				break

		#get class day
		for k, v in days.items():
			if k in line:
				course.update({"day":v})
				break

		#get class time
		for k, v in time.items():
			if k in line:
				course.update({"time":v})
				all_course.append(course.copy())
				break