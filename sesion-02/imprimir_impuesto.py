#!/usr/bin/env python
# -*- encoding: utf8 -*-

def imprimir_impuesto(monto, 
                      moneda='S/.', 
                      porcentaje=0.18, 
                      impuesto='IGV'):
    print "El %s es %s %.2f" % (
        impuesto,
        moneda,
        monto * porcentaje
    )

imprimir_impuesto(100, 'US$', 0.16, "I.V.A.")
