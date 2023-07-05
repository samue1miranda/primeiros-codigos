def somatorio(num):
	soma = 0
	j = 1
	for i in range(1, num + 1):
		if((i%2)==0):
			soma -= pow(i, j)
		else:
			soma += pow(i, j)
		if(j<=2):
			j += 1
		else:
			j = 1
	return soma

def principal():
	termos = int(input())
	while(termos<1):
		termos = int(input())
	print(somatorio(termos))
principal()