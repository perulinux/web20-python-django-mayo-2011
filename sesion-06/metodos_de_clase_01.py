#!/usr/bin/env python
# -*- encoding: utf8 -*-

class Producto(object):

    nombre = ''
    precio = 0.0

    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    @classmethod
    def listar_atributos(cls):
        print "Estoy en la clase: %s" % cls.__name__
        for atributo in dir(cls):
            print atributo

class ProductoPerecible(Producto):

    fecha_expiracion = ''

    def __init__(self, nombre, precio, fecha_expiracion):
        super(ProductoPerecible, self).__init__(
            nombre,
            precio
        )
        self.fecha_expiracion = fecha_expiracion

p1 = Producto("Laptop", 5000)
p2 = ProductoPerecible("Lata de atún", 1.80, '2011-12-31')

p1.listar_atributos()
p2.listar_atributos()
