#!/usr/bin/env python
# -*- encoding: utf8 -*-

class Cosa(object):

    def __init__(self, nombre):
        self.nombre = nombre

class Persona(object):

     def __init__(self, nombre, dni):
             self.nombre = nombre
             self.dni = dni

     def __str__(self):
             return u'%s (%s)' % (self.nombre, self.dni)

if __name__ == '__main__':
    c = Cosa(nombre='Zapatilla')
    print str(c)
    p = Persona(nombre='Juan Perez', dni='10203040')
    print str(p)
