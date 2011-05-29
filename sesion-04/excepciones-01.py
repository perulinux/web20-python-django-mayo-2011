#!/usr/bin/env python
# -*- encoding: utf8 -*-

while True:
    try:        
        texto = raw_input("Ingrese el numero entero: ")
        valor = int(texto)
        print "El valor fue: %d" % valor
        break
    except ValueError, e:
        print "El valor '%s' no es número entero" % texto
        print "Intente nuevamente"
