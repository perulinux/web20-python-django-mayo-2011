#!/usr/bin/env python
# -*- encoding: utf8 -*-

alumnos = (
   {'nombres':'Juan Alberto', 'apellidos':'Perez Galindo'},
   {'nombres':'Juana', 'apellidos':'Ruiz Garcia'},
)

print '\n'.join(["%s, %s" % (alumno['apellidos'], alumno['nombres']) for alumno in alumnos if len(alumno['nombres'])>5])
