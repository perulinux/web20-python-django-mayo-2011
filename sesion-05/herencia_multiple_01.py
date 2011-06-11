#!/usr/bin/env python
# -*- encoding: utf8 -*-

class Terrestre: 
    def desplazar(self):
        print "El animal anda"

class Acuatico: 
    def desplazar(self):
        print "El animal nada"

class Cocodrilo(Terrestre, Acuatico): 
    pass

class Tortuga(Acuatico, Terrestre):
    pass

c = Cocodrilo()
c.desplazar()

t = Tortuga()
t.desplazar()
