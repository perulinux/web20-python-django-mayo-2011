#!/usr/bin/env python
# -*- encoding: utf8 -*-

class MiError(Exception):
    """
    Clase de errores propia de mi aplicación
    """
    pass

def autorizar_ingreso(edad):
    """
    Autoriza el ingreso al sistema
    """
    if edad >= 18:
        return True
    else:
        raise MiError("Ud. es menor de edad")

edad = 17
try:
    autorizar_ingreso(edad)
except MiError, e:
    print "Se produjo un error: %s" % (e)
