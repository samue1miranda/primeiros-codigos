nome = input().split()
salario = list(map(float, input().split()))
horas = list(map(float, input().split()))
n = len(nome)
salario_hora = []
for i in range(n):
	salario_hora.append(salario[i]/horas[i])

max = 0
min = 0
for i in range(n):
	if salario_hora[i] > salario_hora[max]:
		max = i
	if salario_hora[i] < salario_hora[min]:
		min = i

print("maior salario: ", nome[max], salario_hora[max])
print("menor salario: ", nome[min], salario_hora[min])