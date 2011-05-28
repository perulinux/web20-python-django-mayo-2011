#!/usr/bin/env python
# -*- encoding: utf8 -*-

def crear_sumadora(sumando):
    def funcion_temporal(valor):
        return valor + sumando
    return funcion_temporal

def una_sumadora_antes_y_despues(num):
    if num > 0:
        return (
		crear_sumadora(num - 1), 
		crear_sumadora(num), 
		crear_sumadora(num + 1),
	 )
    else:
	return None

a, b, c = una_sumadora_antes_y_despues(10)

print "a: %d b: %d c: %d" % (
	a(10), 
	b(10), 
	c(10)
)

funciones = una_sumadora_antes_y_despues(10)

print "valor 1: %d valor 2: %d valor 3: %d" % (
	funciones[0](10), 
	funciones[1](10), 
	funciones[2](10)
)
