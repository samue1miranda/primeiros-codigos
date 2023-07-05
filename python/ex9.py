def principal():
	qtd = int(input())
	consoantes = 1000
	vogais = ["a", "e", "i", "o", "u", " "]
	for i in range(qtd):
		sugestao = input()
		cont = 0
		for j in range(len(sugestao)):
			for k in range(len(vogais)):
				if(sugestao[j].upper() == vogais[k].upper()):
				break
			else:
				cont+=1
principal()