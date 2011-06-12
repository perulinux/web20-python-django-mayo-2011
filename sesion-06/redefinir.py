#!/usr/bin/env python
# -*- encoding: utf8 -*-

class Padre(object):

    def __init__(self, saludo):
        print saludo

class Hijo(Padre):

    def __init__(self, saludo, despedida):
        super(Hijo, self).__init__(saludo)
        print despedida

p = Padre("Hola")
h = Hijo("Hola", "Chau")
