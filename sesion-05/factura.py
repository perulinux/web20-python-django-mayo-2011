#!/usr/bin/env python
# -*- encoding: utf8 -*-

import functools, operator

class Empresa(object):

    def __init__(self, razon_social, ruc, propietario):
        self.razon_social = razon_social
        self.ruc = ruc
        self.propietario = propietario

class Producto(object):
    
    def __init__(self, descripcion, precio_unitario):
        self.descripcion = descripcion
        self.precio_unitario = precio_unitario

class DetalleFactura(object):

    def __init__(self, producto, cantidad):
        self.producto = producto
        self.cantidad = cantidad

    def subtotal(self):
        """
        Multiplica el precio unitario del producto
        por la cantidad
        """
        return self.producto.precio_unitario * self.cantidad

class Factura(object):

    IGV = 0.18

    def __init__(self, numero, proveedor, cliente):
        self.numero = numero
        self.proveedor = proveedor
        self.cliente = cliente
        self.detalles = []

    def agregar_detalle(self, producto, cantidad):
        self.detalles.append(DetalleFactura(producto, cantidad))

    def total_bruto(self):
        subtotales = [detalle.subtotal() for detalle in self.detalles]
        return functools.reduce(operator.add, subtotales)

    @staticmethod
    def calcular_igv_de_monto(monto):
        return monto * Factura.IGV

    def calcular_igv(self):
        return Factura.calcular_igv_de_monto(self.total_bruto())

    def total_neto(self):
        return self.total_bruto() + self.calcular_igv()

    def imprimir(self):
        print "Factura Nro. %06d" % self.numero
        print "%s - RUC %s" % (
            self.proveedor.razon_social,
            self.proveedor.ruc
        )
        print "De %s" % self.proveedor.propietario
        print
        print "Cliente:"
        print "Razón social: %s" % self.cliente.razon_social
        print "RUC: %s" % self.cliente.ruc
        print
        print "Detalles:"
        print
        print "Descripcion\tCantidad\tPrecio Unitario\tSubtotal"
        for detalle in self.detalles:
            print "%s\t%d\t%.2f\t%.2f" % (
                detalle.producto.descripcion,
                detalle.cantidad,
                detalle.producto.precio_unitario,
                detalle.subtotal()
            )
        print
        print "Monto bruto: S/. %.2f" % self.total_bruto()
        print "IGV: S/. %.2f" % self.calcular_igv()
        print "Monto neto: S/. %.2f" % self.total_neto() 

# Empresas

proveedor = Empresa(
    razon_social='Python S.A.C.',
    ruc='56103420345',
    propietario='Ernesto Quispe'
)

cliente = Empresa(
    'Clevertronix S.A.C.',
    '94324209101',
    propietario='Clever Flores'
)

# Productos

producto1 = Producto(
    descripcion='Laptop MacBook Pro 15"',
    precio_unitario=5000
)

producto2 = Producto(
    descripcion='USB 32 GB HPv3251',
    precio_unitario=150
)

producto3 = Producto(
    'Monitor LCD LG 17"',
    600
)

# Factura

factura = Factura(
    numero=1,
    proveedor=proveedor,
    cliente=cliente
)

factura.agregar_detalle(producto1, 1)
factura.agregar_detalle(producto3, 3)
factura.agregar_detalle(producto2, 2)

factura.imprimir()
