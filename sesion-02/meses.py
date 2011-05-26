#!/usr/bin/env python
# -*- coding: utf8 -*-

def numero_dias_mes(mes):
    if mes in (1, 3, 5, 7, 8, 10, 12, ):
        print u"El mes %d tiene 31 días" % mes
    elif mes in (2, ):
        print u"El mes 2 tiene 28 o 29 días"
    elif mes in [4, 6, 9, 11]:
        print u"El mes %d tiene 30 días" % mes
    else:
        print u"El valor %d esta fuera de rango" % mes

mes = int(raw_input("Ingrese un mes como un número entero: "))

numero_dias_mes(mes)
