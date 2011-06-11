#!/usr/bin/env python
# -*- encoding: utf8 -*-

import operator

def componer_dos_funciones(func1, func2):
    def funcion_auxiliar(valor):
        return func2(func1(valor))
    return funcion_auxiliar

def func1(x):
    return x + 2

func2 = lambda x: x * 2

func3 = componer_dos_funciones(func1, func2)
print func3(10)
