#!/usr/bin/env python
# -*- encoding: utf8 -*-

frase = raw_input("Digite un frase y presione [ENTER]: ")

palabras = frase.split(' ')
palabras_unicas = []

for p in palabras:
    if not p in palabras_unicas:
        palabras_unicas.append(p)

print u"Palabras encontradas: %d" % len(palabras)
print u"Palabras unicas: %d " % len(palabras_unicas)
print 
print u"La lista de palabras únicas es:\n"
for p in palabras_unicas:
    print p
