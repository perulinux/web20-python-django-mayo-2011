# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Incidencia.equipo'
        db.add_column('soporte_incidencia', 'equipo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['hardware.Equipo'], null=True, blank=True), keep_default=False)

        # Adding M2M table for field software on 'Incidencia'
        db.create_table('soporte_incidencia_software', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('incidencia', models.ForeignKey(orm['soporte.incidencia'], null=False)),
            ('software', models.ForeignKey(orm['software.software'], null=False))
        ))
        db.create_unique('soporte_incidencia_software', ['incidencia_id', 'software_id'])


    def backwards(self, orm):
        
        # Deleting field 'Incidencia.equipo'
        db.delete_column('soporte_incidencia', 'equipo_id')

        # Removing M2M table for field software on 'Incidencia'
        db.delete_table('soporte_incidencia_software')


    models = {
        'empresa.area': {
            'Meta': {'object_name': 'Area'},
            'anexo': ('django.db.models.fields.CharField', [], {'max_length': '24', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '64'}),
            'responsable': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'responsables'", 'null': 'True', 'to': "orm['empresa.Empleado']"})
        },
        'empresa.empleado': {
            'Meta': {'ordering': "('apepat', 'apemat', 'nombres')", 'unique_together': "(('doc', 'tipo_doc'),)", 'object_name': 'Empleado'},
            'apemat': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'apepat': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'area': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['empresa.Area']"}),
            'doc': ('django.db.models.fields.CharField', [], {'max_length': '8'}),
            'fecha_nac': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'genero': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombres': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'soporte': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'superior': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['empresa.Empleado']", 'null': 'True', 'blank': 'True'}),
            'telefonos': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'tipo_doc': ('django.db.models.fields.PositiveIntegerField', [], {})
        },
        'empresa.proveedor': {
            'Meta': {'ordering': "('nombre',)", 'object_name': 'Proveedor'},
            'creado_en': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'direccion': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'telefonos': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        'hardware.equipo': {
            'Meta': {'ordering': "('nombre',)", 'object_name': 'Equipo'},
            'creado_en': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'descripcion': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'empleado': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['empresa.Empleado']"}),
            'estado': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'fabricante': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['empresa.Proveedor']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'serie': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'tipo': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['hardware.TipoEquipo']"})
        },
        'hardware.tipoequipo': {
            'Meta': {'ordering': "('nombre',)", 'object_name': 'TipoEquipo'},
            'creado_en': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '64'})
        },
        'software.familiasoftware': {
            'Meta': {'ordering': "('nombre',)", 'object_name': 'FamiliaSoftware'},
            'creado_en': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '64'})
        },
        'software.software': {
            'Meta': {'ordering': "('nombre',)", 'object_name': 'Software'},
            'creado_en': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'descripcion': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'fabricante': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['empresa.Proveedor']"}),
            'familia': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['software.FamiliaSoftware']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '64'}),
            'sistema_operativo': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
        'soporte.adjunto': {
            'Meta': {'object_name': 'Adjunto'},
            'archivo': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'creado_en': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'incidencia': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['soporte.Incidencia']"})
        },
        'soporte.evento': {
            'Meta': {'ordering': "('creado_en',)", 'object_name': 'Evento'},
            'creado_en': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'incidencia': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['soporte.Incidencia']"}),
            'mensaje': ('django.db.models.fields.TextField', [], {}),
            'metadatos': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        'soporte.incidencia': {
            'Meta': {'ordering': "('creado_en',)", 'object_name': 'Incidencia'},
            'asignada_a': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'incidencias_asignadas'", 'null': 'True', 'to': "orm['empresa.Empleado']"}),
            'avance': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'creado_en': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'descripcion': ('django.db.models.fields.TextField', [], {}),
            'equipo': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['hardware.Equipo']", 'null': 'True', 'blank': 'True'}),
            'estado': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'gravedad': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'reportada_por': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'incidencias_reportadas'", 'to': "orm['empresa.Empleado']"}),
            'software': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['software.Software']", 'null': 'True', 'blank': 'True'}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['soporte']
