#!/usr/bin/env python
# -*- encoding: utf8 -*-

import operator

def componer_dos_funciones(func1, func2):
    def funcion_auxiliar(*args, **kwargs):
        return func2(func1(*args, **kwargs))
    return funcion_auxiliar

def func1(x):
    return x + 2

func2 = lambda x: x * 2

func3 = componer_dos_funciones(func1, func2)
print func3(10)

# Aca hay un problema: La primera funcion (suma) solo devuelve
# un valor y la segunda funcion necesita dos.
func4 = componer_dos_funciones(operator.add, operator.sub)

try:
    print func4(100, 40)
except TypeError, e:
    print e

func5 = componer_dos_funciones(operator.add, func1)

print func5(100, 40)
