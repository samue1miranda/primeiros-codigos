ordem = int(input())
matriz = []
for i in range(ordem):
	matriz.append([])
	matriz[i] = list(map(int, input().split()))
soma = 0
meio = int(ordem/2) + 1
for i in range(meio):
	for j in range(i + 1):
		soma += matriz[i][j]
limite = meio - 1
while(meio < ordem):
	for i in range(limite):
		soma += matriz[meio][i]
	meio += 1
	limite -= 1
print(soma)