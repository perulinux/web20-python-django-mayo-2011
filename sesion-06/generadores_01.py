#!/usr/bin/env python
# -*- encoding: utf8 -*-

# Esto seria ineficiente porque si el 
# numero es muy grande ocuparia mucha
# memoria RAM
def generar_lista(max):
    result = []
    for i in range(max):
        result.append(i)
    return result

def mi_generador(n, m, s):

    while(n <= m):
        yield n
        n += s

for x in mi_generador(0, 10, 1):
    print x
