# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Area'
        db.create_table('empresa_area', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(unique=True, max_length=64)),
            ('anexo', self.gf('django.db.models.fields.CharField')(max_length=24, null=True, blank=True)),
            ('responsable', self.gf('django.db.models.fields.related.ForeignKey')(related_name='responsables', to=orm['empresa.Empleado'])),
        ))
        db.send_create_signal('empresa', ['Area'])

        # Adding model 'Empleado'
        db.create_table('empresa_empleado', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('doc', self.gf('django.db.models.fields.CharField')(max_length=8)),
            ('tipo_doc', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('nombres', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('apepat', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('apemat', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('genero', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('telefonos', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('fecha_nac', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('area', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['empresa.Area'])),
            ('superior', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['empresa.Empleado'])),
            ('soporte', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('empresa', ['Empleado'])

        # Adding unique constraint on 'Empleado', fields ['doc', 'tipo_doc']
        db.create_unique('empresa_empleado', ['doc', 'tipo_doc'])


    def backwards(self, orm):
        
        # Removing unique constraint on 'Empleado', fields ['doc', 'tipo_doc']
        db.delete_unique('empresa_empleado', ['doc', 'tipo_doc'])

        # Deleting model 'Area'
        db.delete_table('empresa_area')

        # Deleting model 'Empleado'
        db.delete_table('empresa_empleado')


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
        }
    }

    complete_apps = ['empresa']
