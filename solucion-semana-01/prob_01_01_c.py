#!/usr/bin/env python
# -*- encoding: utf8 -*-

from random import randint

MAX_NUM = 10

menor = None
mayor = None

# Generamos tantos eventos como indique MAX_NUM
for i in range(MAX_NUM):
    numero = randint(1, 10000) 
    # Si es el primero, asignarlo a la
    # variable menor
    if menor is None:
        menor = numero
    if mayor is None:
        mayor = numero
    # Ya tenemos un valor almacenado,
    # ahora nos toca comparar
    if numero < menor:
        menor = numero    
    if numero > mayor:
        mayor = numero

print "El menor número encontrado fué: %d" % menor
print "El mayor número encontrado fué: %d" % mayor
