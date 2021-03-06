# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Book'
        db.create_table(u'book_book', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('metadata', self.gf('django.db.models.fields.TextField')(default='{}')),
            ('settings', self.gf('django.db.models.fields.TextField')(default='{}')),
            ('cover_image', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['usermedia.Image'])),
            ('owner', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
        ))
        db.send_create_signal(u'book', ['Book'])

        # Adding model 'Chapter'
        db.create_table(u'book_chapter', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('text', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['text.Text'])),
            ('book', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['book.Book'])),
            ('number', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'book', ['Chapter'])

        # Adding model 'BookAccessRight'
        db.create_table(u'book_bookaccessright', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('book', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['book.Book'])),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('rights', self.gf('django.db.models.fields.CharField')(max_length=1)),
        ))
        db.send_create_signal(u'book', ['BookAccessRight'])

        # Adding unique constraint on 'BookAccessRight', fields ['book', 'user']
        db.create_unique(u'book_bookaccessright', ['book_id', 'user_id'])


    def backwards(self, orm):
        # Removing unique constraint on 'BookAccessRight', fields ['book', 'user']
        db.delete_unique(u'book_bookaccessright', ['book_id', 'user_id'])

        # Deleting model 'Book'
        db.delete_table(u'book_book')

        # Deleting model 'Chapter'
        db.delete_table(u'book_chapter')

        # Deleting model 'BookAccessRight'
        db.delete_table(u'book_bookaccessright')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'book.book': {
            'Meta': {'object_name': 'Book'},
            'chapters': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['text.Text']", 'through': u"orm['book.Chapter']", 'symmetrical': 'False'}),
            'cover_image': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['usermedia.Image']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'metadata': ('django.db.models.fields.TextField', [], {'default': "'{}'"}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'settings': ('django.db.models.fields.TextField', [], {'default': "'{}'"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        u'book.bookaccessright': {
            'Meta': {'unique_together': "(('book', 'user'),)", 'object_name': 'BookAccessRight'},
            'book': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['book.Book']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'rights': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'book.chapter': {
            'Meta': {'object_name': 'Chapter'},
            'book': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['book.Book']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'number': ('django.db.models.fields.IntegerField', [], {}),
            'text': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['text.Text']"})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'text.text': {
            'Meta': {'object_name': 'Text'},
            'added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'comments': ('django.db.models.fields.TextField', [], {'default': "'[]'"}),
            'contents': ('django.db.models.fields.TextField', [], {}),
            'currently_open': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_accessed': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 6, 14, 0, 0)', 'auto_now': 'True', 'blank': 'True'}),
            'last_editor': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'last_editor'", 'to': u"orm['auth.User']"}),
            'metadata': ('django.db.models.fields.TextField', [], {'default': "'{}'"}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'owner'", 'to': u"orm['auth.User']"}),
            'settings': ('django.db.models.fields.TextField', [], {'default': "'{}'"}),
            'title': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        },
        u'usermedia.image': {
            'Meta': {'object_name': 'Image'},
            'added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'checksum': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '50'}),
            'file_type': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'height': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'image_cat': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'}),
            'thumbnail': ('django.db.models.fields.files.ImageField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'uploader': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'uploader'", 'to': u"orm['auth.User']"}),
            'width': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['book']