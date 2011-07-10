# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'FamiliaSoftware'
        db.create_table('software_familiasoftware', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(unique=True, max_length=64)),
            ('creado_en', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
        ))
        db.send_create_signal('software', ['FamiliaSoftware'])

        # Adding model 'Software'
        db.create_table('software_software', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(unique=True, max_length=64)),
            ('familia', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['software.FamiliaSoftware'])),
            ('fabricante', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['empresa.Proveedor'])),
            ('descripcion', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('sistema_operativo', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('creado_en', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
        ))
        db.send_create_signal('software', ['Software'])


    def backwards(self, orm):
        
        # Deleting model 'FamiliaSoftware'
        db.delete_table('software_familiasoftware')

        # Deleting model 'Software'
        db.delete_table('software_software')


    models = {
        'empresa.proveedor': {
            'Meta': {'ordering': "('nombre',)", 'object_name': 'Proveedor'},
            'creado_en': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'direccion': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'telefonos': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '200'})
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
        }
    }

    complete_apps = ['software']
