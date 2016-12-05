import math

lista =[]
def incio(x,y):
	numero =math.pow(x,y)
	if lista.count(numero)==0:
		lista.append(numero)
	pass

for x in range(2,101):
	for y in range(2,101):
		incio(x,y)
		pass

print "suma",len(lista)



