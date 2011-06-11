#!/usr/bin/env python
# -*- encoding: utf8 -*-

class Persona(object):

    def __init__(self, nombres = '', apepat = '', apemat = ''):
        self.nombres = nombres
        self.apepat = apepat
        self.apemat = apemat

    def nombre_completo(self):
        return "%s %s %s" % (
            self.nombres, 
            self.apepat, 
            self.apemat
        )

    def __str__(self):
        return self.nombre_completo()

p1 = Persona()
p1.nombres = 'Juan Alberto'
p1.apepat = 'Rosales'
p1.apemat = 'Galindo'

print p1.nombre_completo()
print str(p1)
