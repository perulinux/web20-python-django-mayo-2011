#!/usr/bin/env python
# -*- encoding: utf8 -*-

a = 10

def funcion1():

    b = 20

    def sumar_algo():
        b = 50

    sumar_algo()

    print "a vale %d" % a
    print "b vale %d" % b

funcion1()
