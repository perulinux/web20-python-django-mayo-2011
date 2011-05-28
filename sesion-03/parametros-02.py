#!/usr/bin/env python
# -*- encoding: utf8 -*-

def subrayar(texto, caracter='*'):
    print texto
    print len(texto)*caracter 

subrayar('Hola mundo de Python')

subrayar('Programar en Python es facil', '-')

subrayar(caracter='=', texto='PYTHON')
