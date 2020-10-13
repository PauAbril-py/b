a=int(input("Preu:		"))
b=int(input("descompte:	"))
c=input("Descompte percentatge? (y/n):	")
d=b/100*a
if c=="y":
	print(a-d)
elif c=="n":
	print(a-b)