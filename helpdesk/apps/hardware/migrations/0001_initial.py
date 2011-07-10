# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'TipoEquipo'
        db.create_table('hardware_tipoequipo', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('creado_en', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
        ))
        db.send_create_signal('hardware', ['TipoEquipo'])

        # Adding model 'Equipo'
        db.create_table('hardware_equipo', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('tipo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['hardware.TipoEquipo'])),
            ('descripcion', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('empleado', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['empresa.Empleado'])),
            ('serie', self.gf('django.db.models.fields.CharField')(max_length=64, null=True, blank=True)),
            ('fabricante', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['empresa.Proveedor'])),
            ('estado', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
        ))
        db.send_create_signal('hardware', ['Equipo'])


    def backwards(self, orm):
        
        # Deleting model 'TipoEquipo'
        db.delete_table('hardware_tipoequipo')

        # Deleting model 'Equipo'
        db.delete_table('hardware_equipo')


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
        }
    }

    complete_apps = ['hardware']
