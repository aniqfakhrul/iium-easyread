from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
import re
from .models import Course
from datetime import *
from django.db.models import Q

def queries(lines, kulliya):
	days = {
		"MON" : ['Monday'],
		"MW" : ['Monday', 'Wednesday'],
		"UW" : ['Monday', 'Wednesday'],
		"MAW" : ['Monday', 'Wednesday'],
		"TUE" : ["Tuesday"],
		"AH" : ["Tuesday", "Thursday"],
		"T-TH" : ["Tuesday", "Thursday"],
		"0TH" : ["Tuesday", "Thursday"],
		"WED" : ["Wednesday"],
		"THUR" : ["Thursday"],
		"FRI" : ["Friday"],
	}

	time = {
		"500-7" : ['5:00 PM','7:00 PM'],
		"5.00 -7" : ['5:00 PM','7:00 PM'],
		"830 -950" : ['8:30 AM','9:50 AM'],
		"8.30 -9.50" : ['8:30 AM','9:50 AM'],
		"330 -450" : ['3:30 PM','4:50 PM'],
		"3.30 -4.50" : ['3:30 PM','4:50 PM'],
		"1030-1220" : ['10:30 AM','12:20 PM'],
		"10.30 - 12.20" : ['10:30 AM','12:20 PM'],
		"10.00 «11.20" : ['10:00 AM','11:20 AM'],
		"10.00 - 11.20" : ['10:00 AM','11:20 AM'],
		"200 -320" : ['2:00 PM','3:20 PM'],
		"2.00 -3.20" : ['2:00 PM','3:20 PM'],
		"500 -7" : ['5:00 PM','7:00 PM'],
		"11.90 - 1250" : ['11:30 AM','12:50 PM'],
		"3.30 -450" : ['3:30 PM','4:50 PM'],
		"11.30 -1250" : ['11:30 AM','12:50 PM'],
	}
	
	all_course = []
	course = {
		"code" : "",
		"name" : "",
		"day" : [],
		"time" : "",
		"venue" : "",
	}

	posts = Course.objects.filter(Q(kulliya=kulliya) |  Q(uni_required=True))
	for line in lines:
		#get couse code and name
		for post in posts:
			if (post.course_code in line) or (post.course_code.replace(" ","") in line): #check available course code
				course.update({"code" : post.course_code.replace(" ","")})
				course.update({"name" : post.course_name})
				#get class venue
				if re.findall('\\b AM\\b', line):
					course.update({"venue" : line[line.find(' AM')+3:].lstrip()})
				elif re.findall('\\b PM\\b', line):
					course.update({"venue" : line[line.find(' PM')+3:].lstrip().strip("\n")})

				#get class day
				for k, v in days.items():
					if k in line:
						course.update({"day":v})

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