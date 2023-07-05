def arredonda(valor):
	a = int(valor)
	decimal = valor - a
	if decimal > 0.5:
		return a+1
	return a

a =float(input())
b=float(input())
print (arredonda(a))
print (arredonda(b))
