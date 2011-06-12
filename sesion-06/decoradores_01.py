#!/usr/bin/env python
# -*- encoding: utf8 -*-

# Lo que sucede al usar un decorador es que
# Python ejecuta la funcion del decorador pasando
# como argumento la funcion decorada.

# Al ejecutarse el decorador se define una funciona
# auxiliar y se devuelve, de forma que bajo el nombre
# de la funcion decadora existe ahora una nueva funcion
# que es la composicion de la version original de la
# funcion decorada con la funcion auxiliar definidad
# en esa ejecucion del decorador.

def verificar_mayoria_edad(funcion):
    def funcion_auxiliar(edad):
        if edad >= 18:
            funcion(edad)
        else:
            print "Ud. es menor de edad"
    return funcion_auxiliar

@verificar_mayoria_edad
def entrar_al_local(edad):
    print "Ud. esta viendo el show"

entrar_al_local(15)
entrar_al_local(25)
