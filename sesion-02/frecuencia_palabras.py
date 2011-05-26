#!/usr/bin/env python
# -*- encoding: utf8 -*-

frase = raw_input("Digite un frase y presione [ENTER]: ")

palabras = frase.split(' ')
palabras_unicas = []

contadores = {}

for p in palabras:
    if not p in palabras_unicas:
        palabras_unicas.append(p)
        contadores[p] = 1
    else:
        contadores[p] += 1

print u"Palabras encontradas: %d" % len(palabras)
print u"Palabras unicas: %d " % len(palabras_unicas)
print 
print u"La lista de palabras únicas es:\n"
for p in palabras_unicas:
    print "La palabra \"%s\" aparece %d %s" % (
        p,
        contadores[p],
        'vez' if contadores[p] == 1 else 'veces'
    )
