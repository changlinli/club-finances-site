# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Finance_Transaction'
        db.delete_table('finance_entries_finance_transaction')

        # Removing M2M table for field authorizers on 'Finance_Transaction'
        db.delete_table(db.shorten_name('finance_entries_finance_transaction_authorizers'))

        # Adding model 'FinanceTransaction'
        db.create_table('finance_entries_financetransaction', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('heading', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('comments', self.gf('django.db.models.fields.TextField')()),
            ('transaction_time', self.gf('django.db.models.fields.DateField')()),
            ('cleared_by_bank_time', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal('finance_entries', ['FinanceTransaction'])

        # Adding M2M table for field authorizers on 'FinanceTransaction'
        m2m_table_name = db.shorten_name('finance_entries_financetransaction_authorizers')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('financetransaction', models.ForeignKey(orm['finance_entries.financetransaction'], null=False)),
            ('user', models.ForeignKey(orm['auth.user'], null=False))
        ))
        db.create_unique(m2m_table_name, ['financetransaction_id', 'user_id'])


    def backwards(self, orm):
        # Adding model 'Finance_Transaction'
        db.create_table('finance_entries_finance_transaction', (
            ('comments', self.gf('django.db.models.fields.TextField')()),
            ('transaction_time', self.gf('django.db.models.fields.DateField')()),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('cleared_by_bank_time', self.gf('django.db.models.fields.DateField')()),
            ('heading', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('finance_entries', ['Finance_Transaction'])

        # Adding M2M table for field authorizers on 'Finance_Transaction'
        m2m_table_name = db.shorten_name('finance_entries_finance_transaction_authorizers')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('finance_transaction', models.ForeignKey(orm['finance_entries.finance_transaction'], null=False)),
            ('user', models.ForeignKey(orm['auth.user'], null=False))
        ))
        db.create_unique(m2m_table_name, ['finance_transaction_id', 'user_id'])

        # Deleting model 'FinanceTransaction'
        db.delete_table('finance_entries_financetransaction')

        # Removing M2M table for field authorizers on 'FinanceTransaction'
        db.delete_table(db.shorten_name('finance_entries_financetransaction_authorizers'))


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '80', 'unique': 'True'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'to': "orm['auth.Permission']", 'symmetrical': 'False'})
        },
        'auth.permission': {
            'Meta': {'object_name': 'Permission', 'unique_together': "(('content_type', 'codename'),)", 'ordering': "('content_type__app_label', 'content_type__model', 'codename')"},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'blank': 'True', 'max_length': '75'}),
            'first_name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '30'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'to': "orm['auth.Group']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '30'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'to': "orm['auth.Permission']", 'symmetrical': 'False'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '30', 'unique': 'True'})
        },
        'contenttypes.contenttype': {
            'Meta': {'db_table': "'django_content_type'", 'object_name': 'ContentType', 'unique_together': "(('app_label', 'model'),)", 'ordering': "('name',)"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'finance_entries.financetransaction': {
            'Meta': {'object_name': 'FinanceTransaction'},
            'authorizers': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.User']", 'symmetrical': 'False'}),
            'cleared_by_bank_time': ('django.db.models.fields.DateField', [], {}),
            'comments': ('django.db.models.fields.TextField', [], {}),
            'heading': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'transaction_time': ('django.db.models.fields.DateField', [], {})
        }
    }

    complete_apps = ['finance_entries']