def main():
	linhas, colunas = map(int, input().split())
	matriz = list()
	par = 0
	for i in range(linhas):
		matriz.append([]);
		matriz[i] = list(map(float, input().split()))
		for j in range(colunas):
			if(matriz[i][j] % 2 == 0):
				par += 1
	tamanho = linhas * colunas
	impar = tamanho - par
	print(impar)
	print('{0} %'.format(round((impar / tamanho) * 100)))
	print(par)
	print('{0} %'.format(round((par / tamanho) * 100)))
main()