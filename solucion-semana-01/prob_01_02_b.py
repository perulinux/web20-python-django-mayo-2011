#!/usr/bin/env python
# -*- encoding: utf8 -*-
"""
Hallar el valor de la suma de todos los números 
naturales menores que mil que sean divisibles 
simultáneamente por 3 y por 5
"""

def es_divisible(dividendo, divisor):
    return dividendo % divisor == 0

acumulador = 0

divisibles = [numero for numero in range(1000) if (
    es_divisible(numero, 3) and es_divisible(numero, 5)
)]

for numero in divisibles:
    acumulador += numero

print acumulador
