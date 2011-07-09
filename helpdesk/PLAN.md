Plan de Trabajo
===============

Modelos por implementar:

* Proveedor (De hardware, software u otro)
* TipoEquipo (Ej. PC, laptop, servidor, ipad, etc)
* Equipo (Tipo, Serial, Descripción, EmpleadoAsignado, etc)
* FamiliaSoftware (Ej. S.O. Microsoft, Ofimática, Utilitarios, Multimedia)
* Software (con un check si es sistema operativo)
* Area (con un vínculo al empleado responsable del area)
* Empleado (con un vínculo al empleado que es superior inmediato y a la area a la que pertenece además de un boolean que indique si es personal de soporte o no)
* Incidencia
* Comentario (de una incidencia)
* Evento (registro de un cambio de estado en la incidencia - FK incidencia - JSON (de metadatos) - FechaHora - Texto)
* Adjunto (FK a la incidencia)

En clase:

Proveedor

Tarea:

Antonio: Incidencia
Phillyps: Empleado, Area
Samuel: FamiliaSoftware, Software
Jose Antonio: TipoEquipo, Equipo
Christian: Adjunto
Hansy: Evento

División por Django Apps:

empresa

- Area
- Empleado
- Proveedor

hardware

- TipoEquipo
- Equipo

software

- FamilaSoftware
- Software

soporte

- Incidencia
- Evento
- Adjunto

Ayuda tarea:

Correr comandos del manage:

cd project
../env/bin/python manage.py

Para usuar South:

../env/bin/python manage.py schemamigration --initial <nombre_app>
../env/bin/python manage.py migrate

Si tienen cambios:

../env/bin/python manage.py schemamigration --auto <nombre_app>
../env/bin/python manage.py migrate

Para generar el fixture:

../env/bin/python manage.py dumpdata <nombre_app> --indent=4 > ../fixtures/<nombre_app>.json

Para cargar el fixture:

../env/bin/python manage.py loaddata ../fixture/<nombre_app>.json

No olvidar:

- Agregar la nueva app que crean en INSTALLED_APPS dentro de settings

Para ver el proyecto en web:

../env/bin/python manage.py runserver 0.0.0.0:<puerto>
