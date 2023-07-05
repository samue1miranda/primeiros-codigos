linhas, colunas = map(int, input().split())
matriz = []
par = 0
for i in range(linhas):
	matriz.append([]);
	matriz[i] = list(map(float, input().split()))
	for j in range(colunas):
		if(matriz[i][j]%2 == 0):
			par += 1
tamanho = linhas*colunas
impar = tamanho - par
print(impar)
print(round((impar/tamanho)*100), "%")
print(par)
print(round((par/tamanho)*100), "%")