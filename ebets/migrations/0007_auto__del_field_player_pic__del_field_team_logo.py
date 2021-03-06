# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Player.pic'
        db.delete_column(u'ebets_player', 'pic')

        # Deleting field 'Team.logo'
        db.delete_column(u'ebets_team', 'logo')


    def backwards(self, orm):
        # Adding field 'Player.pic'
        db.add_column(u'ebets_player', 'pic',
                      self.gf('django.db.models.fields.CharField')(default=None, max_length=1024),
                      keep_default=False)

        # Adding field 'Team.logo'
        db.add_column(u'ebets_team', 'logo',
                      self.gf('django.db.models.fields.CharField')(default=None, max_length=1024),
                      keep_default=False)


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
            'winner': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'related_name': "'won_matches'", 'to': "orm['ebets.Team']"})
        },
        'ebets.player': {
            'Meta': {'object_name': 'Player'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '5096'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'nickname': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'pic_pattern': ('django.db.models.fields.CharField', [], {'default': "'%s_player_pic_%dx%d'", 'max_length': '255'}),
            'team': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'players'", 'to': "orm['ebets.Team']"})
        },
        'ebets.team': {
            'Meta': {'object_name': 'Team'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '5096'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'logo_pattern': ('django.db.models.fields.CharField', [], {'default': "'%s_team_logo_%dx%d'", 'max_length': '255'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['ebets']