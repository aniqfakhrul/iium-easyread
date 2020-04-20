try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
import re
from datetime import *

query = {}
courses =	{
  "CCSB 3211": "SWIMMING SKILLS 1 (BROTHER)",
  "INFO 3102": "DATA WAREHOUSING",
  "INFO 3305": "WEB APPLICATION DEVELOPMENT",
  "INFO 3501": "PROJECT MANAGEMENT IN IT",
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
# course["time"] = []

image = Image.open('testimage.png')
text = pytesseract.image_to_string(image).upper()
# print(text)
# print (courses)

file = open("text_file","w")
file.write(text)
file.close()

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
				# course['time']['start'] = v[0]
				# course['time']['end'] = v[1]
				v[0] = datetime.strptime(v[0], '%I:%M %p')
				v[0] = datetime.strftime(v[0], "%H:%M")
				v[1] = datetime.strptime(v[1], '%I:%M %p')
				v[1] = datetime.strftime(v[1], "%H:%M")
				innerDict = {"start":str(v[0]), "end":str(v[1])}
				course["time"]=innerDict
				# print (course)
				# course.update({"time":v})
				all_course.append(course.copy())
				break
	return all_course

with open("text_file") as f:
	text = f.readlines()
head = text.index("COURSE SEC STA TITLE CHR DAY TIME VENUE\n")
tail = text.index("ANNOUNCEMENT FROM ACADEMIC MANAGEMENT AND ADMISSION DIVISION\n")
lines = text[head:tail]
queries = queries(lines)
for i in queries:
	print(i['code'] +" : "+ i['name'])
	print(i['day'])
	print("Start: "+i['time']['start'])
	print("End: " + i['time']['end'])
	print(i['venue'])
# print (all_course)


# with open("text_file", 'w') as f:
# 	f.writelines(lines[head:tail])


#write in pdf format
#with open('test.pdf', 'w+b') as f:
#    f.write(pdf) # pdf type is bytes by default






# for k, v in days.items():
# 	if k in line:
# 		days_avail.update({course_id:v})
# 		break

# if not line.startswith(k):