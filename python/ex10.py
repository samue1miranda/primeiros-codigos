def arredonda(valor):
	a = int(valor)
	decimal = valor - a
	return a + 1 if(decimal > 0.5) else a

def main():
	a = float(input())
	b = float(input())
	print(arredonda(a))
	print(arredonda(b))
main()