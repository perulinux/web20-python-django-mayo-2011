#!/usr/bin/env python
# -*- encoding: utf8 -*-

def crear_sumadora(sumando):
    def funcion_temporal(valor):
        return valor + sumando
    return funcion_temporal

sumadora_de_unos = crear_sumadora(1)
sumadora_de_cincos = crear_sumadora(5)

print sumadora_de_unos(1)
print sumadora_de_cincos(10)
