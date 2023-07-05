matriz = []
for i in range(15):
	matriz.append([])
	matriz[i] = list(input().split())
bombas = []
for i in range(3):
	linhas, colunas = map(int, input().split())
	bombas.append(matriz[linhas - 1][colunas - 1])
for i in bombas:
	if(i == "D"):
		print("destroier")
		continue
	if(i == "F"):
		print("fragata")
		continue
	if(i == "L"):
		print("lancha")
		continue
	print("agua")