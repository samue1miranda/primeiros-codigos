def principal():
	lista = list()
	tam = int(input('Digite o tamanho da lista: '))
	for a in range(0, tam):
		a = input('Digite a string a ser inserida: ')
		lista.append(a)
	for i in lista:
		print(i)
principal()
