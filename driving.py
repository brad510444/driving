country = input('請問你來自哪個國家？')
age = input('請問你幾歲？')
age = int(age)

if country == '台灣': #需要加字串的標記
	if age >= 18:
		print('你可以考駕照')
	else:
		print('你不能考駕照')
elif country == '美國':
	if age >= 16:
		print('你可以考駕照')
	else:
		print('你不能考駕照')
else:
	print('只能輸入台灣或美國')
	