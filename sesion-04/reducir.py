#!/usr/bin/env python
# -*- encoding: utf8 -*-

import functools, operator

def reducir(funcion, secuencia, valor_inicial = 0):
    acum = valor_inicial
    for elemento in secuencia:
        acum = funcion(elemento, acum)
    return acum

print reducir(lambda a,b: a + b, [1, 2, 3], 100)

print functools.reduce(operator.add, [1, 2, 3], 100)
