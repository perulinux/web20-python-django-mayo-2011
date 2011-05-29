#!/usr/bin/env python
# -*- encoding: utf8 -*-
"""
Hallar el valor de la suma de todos los números 
naturales menores que mil que sean divisibles 
simultáneamente por 3 y por 5
"""

import functools, operator


divisibles = [numero for numero in range(1000) if (
    numero % 3 == 0 and numero % 5 == 0
)]

resultado = functools.reduce(operator.add, divisibles, 0)
print resultado
