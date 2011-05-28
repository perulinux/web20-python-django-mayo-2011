#!/usr/bin/env python
# -*- encoding: utf8 -*-

def otra(a, b):
    return "a: %s b: %s" % (a, b, )

def varios_argumentos(*args, **kwargs):
    print "*args:"
    print args
    print "**kwargs:"
    print kwargs

def recibir_extras(a, b, **kwargs):
    print "a: %s" % a
    print "b: %s" % b
    print "Otros argumentos con nombre:"
    print kwargs

def modificar_kwargs(**kwargs):
    # kwargs es un diccionario por lo tanto es
    # mutable, pueden agregar mas llaves
    print kwargs

def modificar_args(*args):
    args = list(args)
    args.append(80)
    print args

varios_argumentos(1, 2, 3)

varios_argumentos(20, 30, 40, saludo='hola', despedida='chau')

#otra(1, 2, 3)
#otra(arg1=10, arg2=20)

recibir_extras(10, 20, nombre='Juan')

#recibir_extras(10, 20, a=40, b=50)

modificar_kwargs(x=10, y=20, z=30)

modificar_args(50, 60, 70)
