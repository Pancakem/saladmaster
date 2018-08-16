from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
from .models import TeamRecord, OutputSheet, MailingList, Member
from django.http import HttpResponseRedirect, HttpResponse
import xlwt
import datetime
from django.core.mail import send_mass_mail, EmailMessage



@csrf_protect
def records(request):
    all_records = TeamRecord.objects.all()
    return render(
        request,
        "cpsys/records.html",
        context={"records": all_records},
    )

@login_required
def export_data_excel(request):
	"""
		Formatting and filling excel files
		Allowing download
	"""
	day_list = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
	response = HttpResponse(content_type="application/ms-excel")
	now_ = str(datetime.datetime.now())
	cont = 'attachment; filename="' + now_ + '".xls"'
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

		if rows[1] == 'Bontavita':
			bon_list[1] += int(rows[2])
			bon_list[2] += int(rows[3])
			bon_list[3] += int(rows[4])
			bon_list[4] += int(rows[5])
			bon_list[5] += int(rows[6])
			bon_list[6] += int(rows[7])

		elif rows[1] == 'Red Vortex':
			redv_list[1] += int(rows[2])
			redv_list[2] += int(rows[3])
			redv_list[3] += int(rows[4])
			redv_list[4] += int(rows[5])
			redv_list[5] += int(rows[6])
			redv_list[6] += int(rows[7])

		elif rows[1] == 'Eat Well':
			eat_w_list[1] += int(rows[2])
			eat_w_list[2] += int(rows[3])
			eat_w_list[3] += int(rows[4])
			eat_w_list[4] += int(rows[5])
			eat_w_list[5] += int(rows[6])
			eat_w_list[6] += int(rows[7])

		elif rows[1] == 'Food Matters':
			food_list[1] += int(rows[2])
			food_list[2] += int(rows[3])
			food_list[3] += int(rows[4])
			food_list[4] += int(rows[5])
			food_list[5] += int(rows[6])
			food_list[6] += int(rows[7])

		elif rows[1] == 'Warriors':
			warr_list[1] += int(rows[2])
			warr_list[2] += int(rows[3])
			warr_list[3] += int(rows[4])
			warr_list[4] += int(rows[5])
			warr_list[5] += int(rows[6])
			warr_list[6] += int(rows[7])

		elif rows[1] == 'HealthLine':
			hl_list[1] += int(rows[2])
			hl_list[2] += int(rows[3])
			hl_list[3] += int(rows[4])
			hl_list[4] += int(rows[5])
			hl_list[5] += int(rows[6])
			hl_list[6] += int(rows[7])

		elif rows[1] == 'Gold':
			gold_list[1] += int(rows[2])
			gold_list[2] += int(rows[3])
			gold_list[3] += int(rows[4])
			gold_list[4] += int(rows[5])
			gold_list[5] += int(rows[6])
			gold_list[6] += int(rows[7])

		elif rows[1] == 'Avator':
			av_list[1] += int(rows[2])
			av_list[2] += int(rows[3])
			av_list[3] += int(rows[4])
			av_list[4] += int(rows[5])
			av_list[5] += int(rows[6])
			av_list[6] += int(rows[7])

		elif rows[1] == 'LCL':
			lcl_list[1] += int(rows[2])
			lcl_list[2] += int(rows[3])
			lcl_list[3] += int(rows[4])
			lcl_list[4] += int(rows[5])
			lcl_list[5] += int(rows[6])
			lcl_list[6] += int(rows[7])

		elif rows[1] == 'Mezani':
			meza_list[1] += int(rows[2])
			meza_list[2] += int(rows[3])
			meza_list[3] += int(rows[4])
			meza_list[4] += int(rows[5])
			meza_list[5] += int(rows[6])
			meza_list[6] += int(rows[7])

		elif rows[1] == 'Red 5':
			red5_list[1] += int(rows[2])
			red5_list[2] += int(rows[3])
			red5_list[3] += int(rows[4])
			red5_list[4] += int(rows[5])
			red5_list[5] += int(rows[6])
			red5_list[6] += int(rows[7])

		elif rows[1] == 'Nourish Tanzania':
			nt_list[1] += int(rows[2])
			nt_list[2] += int(rows[3])
			nt_list[3] += int(rows[4])
			nt_list[4] += int(rows[5])
			nt_list[5] += int(rows[6])
			nt_list[6] += int(rows[7])

		elif rows[1] == 'Joash Investment':
			ji_list[1] += int(rows[2])
			ji_list[2] += int(rows[3])
			ji_list[3] += int(rows[4])
			ji_list[4] += int(rows[5])
			ji_list[5] += int(rows[6])
			ji_list[6] += int(rows[7])

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



	wb.save(response)
	recipient_list = MailingList.objects.all().values_list('email')

	return response
        