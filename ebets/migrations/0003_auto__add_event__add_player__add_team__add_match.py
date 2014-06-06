# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Event'
        db.create_table(u'ebets_event', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=1024)),
            ('logo', self.gf('django.db.models.fields.CharField')(max_length=1024)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=5096)),
            ('online', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('offline', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('ebets', ['Event'])

        # Adding model 'Player'
        db.create_table(u'ebets_player', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nickname', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('team', self.gf('django.db.models.fields.related.ForeignKey')(related_name='players', to=orm['ebets.Team'])),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('pic', self.gf('django.db.models.fields.CharField')(max_length=1024)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=5096)),
        ))
        db.send_create_signal('ebets', ['Player'])

        # Adding model 'Team'
        db.create_table(u'ebets_team', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=5096)),
            ('logo', self.gf('django.db.models.fields.CharField')(max_length=1024)),
        ))
        db.send_create_signal('ebets', ['Team'])

        # Adding model 'Match'
        db.create_table(u'ebets_match', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('radiant', self.gf('django.db.models.fields.related.ForeignKey')(related_name='radiant_matches', to=orm['ebets.Team'])),
            ('dire', self.gf('django.db.models.fields.related.ForeignKey')(related_name='dire_matches', to=orm['ebets.Team'])),
            ('date', self.gf('django.db.models.fields.DateTimeField')(default=False)),
            ('event', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ebets.Event'])),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=5096)),
            ('winner', self.gf('django.db.models.fields.related.ForeignKey')(related_name='won_matches', to=orm['ebets.Team'])),
            ('over', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('ebets', ['Match'])


    def backwards(self, orm):
        # Deleting model 'Event'
        db.delete_table(u'ebets_event')

        # Deleting model 'Player'
        db.delete_table(u'ebets_player')

        # Deleting model 'Team'
        db.delete_table(u'ebets_team')

        # Deleting model 'Match'
        db.delete_table(u'ebets_match')


    models = {
        'ebets.event': {
            'Meta': {'object_name': 'Event'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '5096'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'logo': ('django.db.models.fields.CharField', [], {'max_length': '1024'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '1024'}),
            'offline': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'online': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
        'ebets.match': {
            'Meta': {'object_name': 'Match'},
            'date': ('django.db.models.fields.DateTimeField', [], {'default': 'False'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '5096'}),
            'dire': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'dire_matches'", 'to': "orm['ebets.Team']"}),
            'event': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ebets.Event']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'over': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'radiant': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'radiant_matches'", 'to': "orm['ebets.Team']"}),
            'winner': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'won_matches'", 'to': "orm['ebets.Team']"})
        },
        'ebets.player': {
            'Meta': {'object_name': 'Player'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '5096'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'nickname': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'pic': ('django.db.models.fields.CharField', [], {'max_length': '1024'}),
            'team': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'players'", 'to': "orm['ebets.Team']"})
        },
        'ebets.team': {
            'Meta': {'object_name': 'Team'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '5096'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'logo': ('django.db.models.fields.CharField', [], {'max_length': '1024'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['ebets']