#!/usr/bin/env python
# -*- encoding: utf8 -*-

def sumar(a, b):
    return a + b

operacion_suma = sumar

print operacion_suma(1, 1)

def aplicar_a_lista(lista, funcion):
    nueva_lista = []
    for elemento in lista:
        nueva_lista.append(funcion(elemento))
    return nueva_lista

def sumar_uno(elemento):
    return elemento + 1

print aplicar_a_lista([1, 2, 3], sumar_uno)

def crear_funcion():
    def sumar_dos(elemento):
        return elemento + 2
    return sumar_dos

sumar_dos = crear_funcion()

print sumar_dos(2)
