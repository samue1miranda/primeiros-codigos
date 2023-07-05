#!/usr/bin/env python
import sys
def func(a):
	return 2*a
def principal():
	lista=[]
	n=input('digite o tamanho da lista: ')
	for a in range(0, n):
		a=raw_input('digite a string a ser inserida: ')
		lista.append(a)
	for i in lista:
		print (i)
	func(sys.argv[1])

