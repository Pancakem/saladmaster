from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
from .models import TeamRecord, OutputSheet, MailingList, Member
from django.http import HttpResponseRedirect, HttpResponse
import xlwt
import datetime
from django.core.mail import send_mass_mail, EmailMessage, get_connection



day_list = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

# uncomment to add cover page
# @csrf_protect
# def records(request):

#     all_records = TeamRecord.objects.all()
#     return render(
#         request,
#         "cpsys/records.html",
#         context={"records": all_records},
#     )

def add_index(_list, other_list):
	""" Does index addition for lists"""

	for i in range(6):
		_list[i+1] += int(other_list[i+2])
	

def switch(_list, other_list, keyword):
	""" Handles multiple if else logic for multiple lists"""

	if other_list[1] == keyword:
		add_index(_list, other_list)

def send(recipient_list, filename):

	connection = get_connection()
	email = EmailMessage(
		'Dinner Report ' + day_list[datetime.datetime.weekday(datetime.datetime.now())],
		'Please find attached below',
		'oumamarvin@gmail.com',
		recipient_list,
		attachments=filename,
		connection=connection)
	email.send()
	connection.close()

def write_file():
	""""
	Writes excel object to dwonload stream"""
	
	global day_list

	response = HttpResponse(content_type="application/ms-excel") 

	now_ = "Dinner_Report " + day_list[datetime.datetime.weekday(datetime.datetime.now())] + ".xls" 

	cont = 'attachment; filename="'"Dinner_Report " + day_list[datetime.datetime.weekday(datetime.datetime.now())] + '".xls"'

	response["Content-Disposition"] = cont

	wb = xlwt.Workbook(encoding="utf-8")
	# the weekday sheet for daily reports
	ws = wb.add_sheet(day_list[datetime.date.weekday(datetime.datetime.now())])
	
	row_num = 0

	font_style = xlwt.XFStyle()
	font_style.font.bold = True

	columns = ['NAME', 'TEAM', 'B', 'CA', 'RE', 'C', 'S', 'D']
	
	for col_num in range(len(columns)):
	    ws.write(row_num, col_num, columns[col_num], font_style)

	font_style = xlwt.XFStyle()
	for_row = OutputSheet.objects.all().values_list('member', 'booking', 'CA', 'recruited', 'cooking', 'sets', 'dinner')
	rows = list()
	booking_total, ca_total, recruited_total, cooking_total, sets_total, dinner_total = 0, 0, 0, 0, 0, 0

	bon_list, redv_list, eat_w_list = ["Bontavita", 0,0,0,0,0,0], ["Red Vortex", 0,0,0,0,0,0], ["Eat Well", 0,0,0,0,0,0]
	food_list, warr_list, nt_list = ["Food Matters",0,0,0,0,0,0], ["Warriors", 0,0,0,0,0,0], ["Nourish Tanzania", 0,0,0,0,0,0]
	hl_list, gold_list, av_list, = ["HealthLine",0,0,0,0,0,0], ["Gold",0,0,0,0,0,0], ["Avator",0,0,0,0,0,0]
	lcl_list, meza_list, red5_list, ji_list = ["LCL",0,0,0,0,0,0], ["Mezani",0,0,0,0,0,0], ["Red 5",0,0,0,0,0,0], ["Joash Investment",0,0,0,0,0,0]
	for_row = list(for_row)
	a = len(for_row)
	all_tup = list()
	i = 1
	for j in range(len(for_row)):
		booking_total += for_row[j][1]
		ca_total += for_row[j][2]
		recruited_total += for_row[j][3]
		cooking_total += for_row[j][4]
		sets_total += for_row[j][5]
		dinner_total += for_row[j][6]

		person = Member.objects.filter(member_id=for_row[j][0]).values_list('first_name', 'last_name', 'team')
		person = list(person)
		rows.append(str(person[0][0] + " " + person[0][1]))
		rows.append(str(person[0][2]))
	
		while i < len(for_row[j]):
			rows.append(str(for_row[j][i]))
			i += 1

		switch(bon_list, rows, 'Bontavita')
		switch(redv_list, rows, 'Red Vortex')
		switch(eat_w_list, rows, 'Eat Well')
		switch(food_list, rows, 'Food Matters')
		switch(warr_list, rows, 'Warriors')
		switch(hl_list, rows, 'Healthline')
		switch(gold_list, rows, 'Gold')
		switch(av_list, rows, 'Avator')
		switch(lcl_list, rows, 'LCL')
		switch(meza_list, rows, 'Mezani')
		switch(red5_list, rows, 'Red 5')
		switch(nt_list, rows,'Nourish Tanzania')
		switch(ji_list, rows, 'Joash Investment')

		all_tup.append(rows)
		rows = []
		i = 1
	
	for row in all_tup:
		row_num += 1
		for col_num in range(len(row)):
			ws.write(row_num, col_num, row[col_num], font_style)
	row_num = 0
	sum_list = [
				ji_list, gold_list, red5_list, redv_list,
				nt_list, bon_list, meza_list, lcl_list,
				av_list, hl_list, eat_w_list, warr_list, food_list
				 ]
	# the summary sheet
	ws2 = wb.add_sheet('Summary')
	cols = ['TEAM', 'B', 'CA', 'RE', 'C', 'S', 'D']
	total_list = list(["Total", booking_total, ca_total, recruited_total, cooking_total, sets_total, dinner_total])
	
	for col_num in range(len(cols)):
		font_style.font.bold = True
		ws2.write(0, col_num, cols[col_num], font_style)
		font_style = xlwt.XFStyle()
	
	for row in sum_list:
		row_num += 1
		for col_num in range(len(row)):
			ws2.write(row_num, col_num, row[col_num], font_style)


	for col_num in range(len(cols)):
		font_style.font.bold = True
		ws2.write(row_num+3, col_num, total_list[col_num], font_style)
	font_style = xlwt.XFStyle()
	
	
	recipient_list = MailingList.objects.all().values_list('email')
	filename = now_
	try:
		wb.save(filename)
		send(recipient_list, filename)
	except Exception as e:
		print(e)
		wb.save(response)
	wb.save(response)
	return response
	


@login_required
def export_data_excel(request):
	"""
		Formatting and add_indexing excel files
		Allowing download
	"""
	# delete the entries in the table at end week
	if day_list[datetime.date.weekday(datetime.datetime.now())].lower() == 'friday':
		OutputSheet.objects.all().delete()

	return write_file()

