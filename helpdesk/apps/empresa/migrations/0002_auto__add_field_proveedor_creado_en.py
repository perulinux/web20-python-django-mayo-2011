# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Proveedor.creado_en'
        db.add_column('empresa_proveedor', 'creado_en', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Proveedor.creado_en'
        db.delete_column('empresa_proveedor', 'creado_en')


    models = {
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
