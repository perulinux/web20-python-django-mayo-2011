#!/usr/bin/env python
# -*- encoding: utf8 -*-

def imprimir_parametros(**kwargs):
    print kwargs

def sumar_e_imprimir(a, b, **kwargs):
    print a + b
    kwargs['a'] = a
    kwargs['b'] = b
    imprimir_parametros(**kwargs)

def prueba_argumentos(a, b, c, d, e):
    print "a: %s" % a
    print "b: %s" % b
    print "c: %s" % c
    print "d: %s" % d
    print "e: %s" % e

def opcionales(a=10, b=20, c=30):
    print "Llamada a la funcion 'opcionales':"
    print "a: %s" % a
    print "b: %s" % b
    print "c: %s" % c

params = {}
params['a'] = 10
params['b'] = 20

imprimir_parametros(**params)

sumar_e_imprimir(5, 5, saludo='hola', x=40)

#sumar_e_imprimir(10, a=40, x=50)

prueba_argumentos(a=10, c=30, e=50, b=20, d=40) 

opcionales(c=50)

parametros = (100, 200, 300,)
opcionales(*parametros)

params1 = (10, )
params2 = {'c': 50, 'b': 80}

opcionales(*params1, **params2)
# es como si Python reemplazara esto -> opcionales(10, c=50, b=80)
