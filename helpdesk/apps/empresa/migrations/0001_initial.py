# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Proveedor'
        db.create_table('empresa_proveedor', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('website', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('direccion', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('telefonos', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal('empresa', ['Proveedor'])


    def backwards(self, orm):
        
        # Deleting model 'Proveedor'
        db.delete_table('empresa_proveedor')


    models = {
        'empresa.proveedor': {
            'Meta': {'ordering': "('nombre',)", 'object_name': 'Proveedor'},
            'direccion': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'telefonos': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['empresa']
