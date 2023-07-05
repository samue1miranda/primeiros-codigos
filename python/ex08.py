def somatorio(num):
	soma = 0
	j = 1
	for i in range(1, num + 1):
		soma = (soma - pow(i, j)) if(i%2 == 0) else (soma + pow(i, j))
		j = (j + 1) if(j < 2) else 1
	return soma

def principal():
	termos = int(input())
	while(termos<1):
		termos = int(input())
	print(somatorio(termos))
principal()