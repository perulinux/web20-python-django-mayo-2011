#!/usr/bin/env python
# -*- encoding: utf8 -*-

class VotoViciadoError(Exception):
    pass 

def get_votos_validos_2da_vuelta():
    return ['K','O']

def votar(voto):
    if not voto in get_votos_validos_2da_vuelta():
        raise VotoViciadoError(
            "El voto por %s se considera viciado" \
            % voto
        )
    print "El voto fue por %s" % voto

try:
    voto = raw_input("Ingrese su voto: ")
    votar(voto)
except VotoViciadoError, e:
    print e
