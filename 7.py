import math

a=int(input("A:	"))
b=int(input("B:	"))
c=int(input("C:	"))

if a == 0:
	print("no se puede calcular")
else:
	if b**2-4*a*c > 0:
		sqrt = math.sqrt(b**2-4*a*c)
		qp = (-b)+sqrt
		qn = (-b)-sqrt
		w = 2*a
		xp = qp/w
		xn = qn/w
		print(xp,xn)
	else:
		print("no se puede calcular")