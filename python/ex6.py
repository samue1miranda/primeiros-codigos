def principal():
	nome = input().split()
	salario = list(map(float, input().split()))
	horas = list(map(float, input().split()))
	n = len(nome)
	salario_hora = list()
	for i in range(n):
		salario_hora.append(salario[i]/horas[i])

	max, min = 0, 0
	for i in range(n):
		if salario_hora[i] > salario_hora[max]:
			max = i
		if salario_hora[i] < salario_hora[min]:
			min = i

	print("maior salario: {0}, {1}".format(nome[max], salario_hora[max]))
	print("menor salario: {0}, {1}".format(nome[min], salario_hora[min]))
principal()