# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Incidencia'
        db.create_table('soporte_incidencia', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('titulo', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('gravedad', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('estado', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('descripcion', self.gf('django.db.models.fields.TextField')()),
            ('reportada_por', self.gf('django.db.models.fields.related.ForeignKey')(related_name='incidencias_reportadas', to=orm['empresa.Empleado'])),
            ('asignada_a', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='incidencias_asignadas', null=True, to=orm['empresa.Empleado'])),
            ('avance', self.gf('django.db.models.fields.FloatField')(default=0.0)),
            ('creado_en', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
        ))
        db.send_create_signal('soporte', ['Incidencia'])

        # Adding model 'Evento'
        db.create_table('soporte_evento', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('incidencia', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['soporte.Incidencia'])),
            ('mensaje', self.gf('django.db.models.fields.TextField')()),
            ('metadatos', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('creado_en', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
        ))
        db.send_create_signal('soporte', ['Evento'])

        # Adding model 'Adjunto'
        db.create_table('soporte_adjunto', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('incidencia', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['soporte.Incidencia'])),
            ('archivo', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('creado_en', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
        ))
        db.send_create_signal('soporte', ['Adjunto'])


    def backwards(self, orm):
        
        # Deleting model 'Incidencia'
        db.delete_table('soporte_incidencia')

        # Deleting model 'Evento'
        db.delete_table('soporte_evento')

        # Deleting model 'Adjunto'
        db.delete_table('soporte_adjunto')


    models = {
        'empresa.area': {
            'Meta': {'object_name': 'Area'},
            'anexo': ('django.db.models.fields.CharField', [], {'max_length': '24', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '64'}),
            'responsable': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'responsables'", 'to': "orm['empresa.Empleado']"})
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
            'superior': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['empresa.Empleado']"}),
            'telefonos': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'tipo_doc': ('django.db.models.fields.PositiveIntegerField', [], {})
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
            'estado': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'gravedad': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'reportada_por': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'incidencias_reportadas'", 'to': "orm['empresa.Empleado']"}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['soporte']
