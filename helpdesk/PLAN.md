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

Para el 16 de Julio:

Listado de incidencias (vista para usuarios finales)

Responsables:

Christian
Jose Antonio

- vista en la aplicación "soporte" que muestre un listado de las incidencias reportadas por el usuario que ha iniciado sesión
- vista de detalle de la incidencia (para usuario final) incluyendo que personal lo tiene asignado, porcentaje de avance, documentos adjuntos, y el listado de eventos ordenado descendentemente.
- Formulario para reportar un nuevo incidente (ModelForm) en una vista que recibe el form y crea la incidencia

Listado de incidencias (vista para personal de soporte)

Responsables:

Phyllips
Samuel

- Listado de incidencias reportadas indicando si esta asignada o no y a aquien ha sido asignada
- Se marca con un color especial las incidencias asignas al usuario de soporte que esta logueado
- Hacer un formulario para actualizar el estado de la incidencia en donde el combo para escoger al usuario asignado solo muestra usuarios que son de soporte (ModelChoiceField)
- Usar un manager para filtrar solo al personal de soporte
- Hay que hacer la vista para el listado y la vista para actualizar la 
incidencia:

Antonio:

- Mejorar el admin de incidencias incluyendo "inlines" 
- Escribir el código que detecta los cambios de estado, escribe el mensaje relacionado y la metada y lo guarda en la base de datos.
- Avanzado la integración con pantallas de login, logout, recuperar password.

Para el domingo (última clase)

- Reportes (intentaremos exportar como CSV)
- Gráficos (usando Google Chart API)
