def inicial_maiuscula(lista):
	for nome in lista:
		a += len(nome)
	return lista

def upper_list(lista):
	for nome in lista:
		a = nome.upper()
		print(a)
		print(nome)
		lista.remove(nome)
		lista.append(a)
	return lista

li = ["samuel", "miranda", "carvalhais"]

print(li)
inicial_maiuscula(li)
print(upper_list(li))
print(li)
