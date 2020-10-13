import calendar

a=int(input("DD		"))
b=int(input("MM		"))
c=int(input("AAAA	"))
d=int(input("HH		"))
e=int(input("MnMn	"))
f=int(input("SS		"))


#	add time
def add():
#	min
	if e == 59:
		e=0
#	hora
	if d == 23:
		d=0
#	dia
	if b == 1 or b==3 or b==5 or b==7 or b==8 or b==10 or b==12:
		if a==31:
			a=0
			if b == 12:
				b=0
			else:
				b=b+1
	elif b==4 or b==6 or b==9 or b==11:
		if a==30:
			a=0
			b=b+1
	elif b==2:
		if calendar.isleap(c):
			if a==29:
				a=0
				b=b+1
		elif not calendar.isleap(c):
			if a==28:
				a=0
				b=b+1



#add a second
if c<=9999 and c>=0:
	if b==1 or b==3 or b==5 or b==7 or b==8 or b==10 or b==12:
		if a<=31 and a>=0:
			if d <= 24 and d >= 0:
				if e <=60 and e>= 0:
					if f == 59:
						add()
						print(a,b,c,e,f)
					elif f < 58 and f > 0:
						print(a,b,c,e,f+1)
		else:
			print("la data es incorrecta")
	elif b==4 or b==6 or b==9 or b==11:
		if a<=30 and a>=0:
			if d <= 24 and d >= 0:
				if e <=60 and e>= 0:
					if f == 60:
						print(a,b,c,d,e,0)
					elif f < 60 and f > 0:
						print(a,b,c,e,f+1)
		else:
			print("la data es incorrecta")
	elif b==2:
		if calendar.isleap(c):
			if a<=29 and a>=0:
				if d <= 24 and d >= 0:
					if e <=60 and e>= 0:
						if f == 60:
							print(a,b,c,d,e,0)
						elif f < 60 and f > 0:
							print(a,b,c,e,f+1)
			else:
				print("la data es incorrecta")
		elif not calendar.isleap(c):
			if a<=28 and a>=0:
				if d <= 24 and d >= 0:
					if e <=60 and e>= 0:
						if f == 60:
							print(a,b,c,d,e,0)
						elif f < 60 and f > 0:
							print(a,b,c,e,f+1)
			else:
				print("la data es incorrecta")