#!/usr/bin/env python
# -*- encoding: utf8 -*-

# Para crear un decorador con argumentos se
# crea una funcion que reciba los argumentos
# y que devuelva un decorador que use esos
# argumento

def verificar_edad_minima(edad_minima = 18):

    def decorador(funcion):
        def funcion_auxiliar(edad):
            if edad >= edad_minima:
                funcion(edad)
            else:
                print "Ud. es menor de edad"
        return funcion_auxiliar

    def resultado(funcion):
        return decorador(funcion)
        
    # return lambda f: decorador(f)

    return resultado

@verificar_edad_minima(21)
def entrar_al_local(edad):
    print "Ud. esta viendo el show"

entrar_al_local(15)
entrar_al_local(25)
