matriz = []
total = 0
obediente = 0
rico = 0
for i in range(3):
	matriz.append([])
	matriz[i] = list(map(float, input().split()))
	soma = 0
	for j in matriz[i]:
		soma += j
	if(soma > rico):
		rico = soma
		obediente = i
	total += soma
print(total/3)
nomes = ["Joãozinho", "Zezinho", "Mariazinha"]
print(nomes[obediente], rico)