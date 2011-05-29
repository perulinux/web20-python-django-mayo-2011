#!/usr/bin/env python
# -*- encoding: utf8 -*-

class ErrorConLog(Exception):

    def __init__(self, message):
        self.message = message
        f = open("/tmp/excepciones.log", "a")
        f.write(message + "\n")

edad = 17

if edad <= 18:
    raise ErrorConLog("El usuario es menor de edad")

