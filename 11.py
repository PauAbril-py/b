import calendar

a=int(input("DD		"))
b=int(input("MM		"))
c=int(input("AAAA	"))
d=int(input("HH		"))
e=int(input("MnMn	"))
f=int(input("SS		"))
q=0
w=0
print()

# comprobar data
if c<=9999 and c>=0:
	if b==1 or b==3 or b==5 or b==7 or b==8 or b==10 or b==12:
		if a<=31 and a>=1:
			q=1
	elif b==4 or b==6 or b==9 or b==11:
		if a<=30 and a>=1:
			q=1
	elif b==2:
		if calendar.isleap(c):
			if a<=29 and a>=1:
				q=1
		elif not calendar.isleap(c):
			if a<=28 and a>=1:
				q=1

#	comprovar hora
if d<=23 and d>=0:
	if e<=59 and e>=0:
		if f<=59 and f>=0:
			w=1

#	sumar 1 segon
if q==1 and w==1:
	if f == 59:
#	min
		if e == 59:
			e="00"
			d=d+1
		else:
			e=e+1
#	hora
		if d == 24:
			d="00"
			a=a+1
#	any/mes/dia
		if b == 1 or b==3 or b==5 or b==7 or b==8 or b==10 or b==12:
			if a ==32:
				a=1
				if b == 12:
					b=1
					c=c+1
				else:
					b=b+1
		elif b==4 or b==6 or b==9 or b==11:
			if a==31:
				a=1
				b=b+1
		elif b==2:
			if calendar.isleap(c):
				if a==30:
					a=1
					b=b+1
			elif not calendar.isleap(c):
				if a==29:
					a=1
					b=b+1
#	segon
		f="00"
		print(a,"/",b,"/",c," ",d,":",e,".",f)
	elif f < 58 and f > 0:
		print(a,"/",b,"/",c," ",d,":",e,".",f+1)
else:
	print("La data es incorrecta.")