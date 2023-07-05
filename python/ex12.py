def imprime_cardapio(pratos):
	"Procedimento para impressao do cardapio"
	print("Cardapio do dia\n")
	for p in pratos:
		imprime_prato(p)
	print("\nTotal de pratos: %d" % len(pratos))

def imprime_prato(p):
	"Procedimento para impressao do prato"
	print("%20s ........... %6.2f" % (p["nome"], p["preço"]))

def principal():
	p1 = {"nome" : "Arroz com brocolis", "preço" : 9.90}
	p2 = {"nome" : "Sopa de legumes", "preço" : 8.70}
	p3 = {"nome" : "Lentilhas", "preço" : 7.80}
	lista_pratos = [p1, p2, p3]
	imprime_cardapio(lista_pratos)
	for prato in lista_pratos:
		imprime_prato(prato)
principal()