a=int(input("caprabo		"))
b=int(input("menys		"))
c=int(input("ano			"))

if c<9999 and c>0:
	if b==1 or b==3 or b==5 or b==7 or b==8 or b==10 or b==12:
		if a<31 and a>0:
			print("la data es correcta")
		else:
			print("la data es incorrecta")
	elif b==4 or b==6 or b==9 or b==11:
		if a<30 and a>0:
			print("la data es correcta")
		else:
			print("la data es incorrecta")
	elif b==2:
		if a<28 and a>0:
			print("la data es correcta")
		else:
			print("la data es incorrecta")