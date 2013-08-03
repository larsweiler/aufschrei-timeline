# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'User'
        db.create_table(u'timeline_user', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('image_url', self.gf('django.db.models.fields.URLField')(max_length=400)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal(u'timeline', ['User'])

        # Adding model 'Hashtag'
        db.create_table(u'timeline_hashtag', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=160)),
        ))
        db.send_create_signal(u'timeline', ['Hashtag'])

        # Adding model 'Analysis'
        db.create_table(u'timeline_analysis', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=160)),
        ))
        db.send_create_signal(u'timeline', ['Analysis'])

        # Adding model 'URL'
        db.create_table(u'timeline_url', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('shorturl', self.gf('django.db.models.fields.URLField')(max_length=30)),
            ('longurl', self.gf('django.db.models.fields.URLField')(max_length=1000)),
            ('faviconurl', self.gf('django.db.models.fields.URLField')(default='', max_length=1000)),
            ('title', self.gf('django.db.models.fields.CharField')(default='', max_length=1000)),
        ))
        db.send_create_signal(u'timeline', ['URL'])

        # Adding model 'Image'
        db.create_table(u'timeline_image', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('image_url', self.gf('django.db.models.fields.URLField')(max_length=400)),
        ))
        db.send_create_signal(u'timeline', ['Image'])

        # Adding model 'Tweet'
        db.create_table(u'timeline_tweet', (
            ('tweet_id', self.gf('django.db.models.fields.BigIntegerField')(unique=True, primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['timeline.User'])),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')()),
            ('text', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('source', self.gf('django.db.models.fields.CharField')(max_length=400)),
            ('in_reply_to', self.gf('django.db.models.fields.BigIntegerField')(null=True, blank=True)),
            ('geo_coordinates', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('retweet', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'timeline', ['Tweet'])

        # Adding M2M table for field hashtags on 'Tweet'
        m2m_table_name = db.shorten_name(u'timeline_tweet_hashtags')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('tweet', models.ForeignKey(orm[u'timeline.tweet'], null=False)),
            ('hashtag', models.ForeignKey(orm[u'timeline.hashtag'], null=False))
        ))
        db.create_unique(m2m_table_name, ['tweet_id', 'hashtag_id'])

        # Adding M2M table for field analysis on 'Tweet'
        m2m_table_name = db.shorten_name(u'timeline_tweet_analysis')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('tweet', models.ForeignKey(orm[u'timeline.tweet'], null=False)),
            ('analysis', models.ForeignKey(orm[u'timeline.analysis'], null=False))
        ))
        db.create_unique(m2m_table_name, ['tweet_id', 'analysis_id'])

        # Adding M2M table for field url on 'Tweet'
        m2m_table_name = db.shorten_name(u'timeline_tweet_url')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('tweet', models.ForeignKey(orm[u'timeline.tweet'], null=False)),
            ('url', models.ForeignKey(orm[u'timeline.url'], null=False))
        ))
        db.create_unique(m2m_table_name, ['tweet_id', 'url_id'])

        # Adding M2M table for field image on 'Tweet'
        m2m_table_name = db.shorten_name(u'timeline_tweet_image')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('tweet', models.ForeignKey(orm[u'timeline.tweet'], null=False)),
            ('image', models.ForeignKey(orm[u'timeline.image'], null=False))
        ))
        db.create_unique(m2m_table_name, ['tweet_id', 'image_id'])


    def backwards(self, orm):
        # Deleting model 'User'
        db.delete_table(u'timeline_user')

        # Deleting model 'Hashtag'
        db.delete_table(u'timeline_hashtag')

        # Deleting model 'Analysis'
        db.delete_table(u'timeline_analysis')

        # Deleting model 'URL'
        db.delete_table(u'timeline_url')

        # Deleting model 'Image'
        db.delete_table(u'timeline_image')

        # Deleting model 'Tweet'
        db.delete_table(u'timeline_tweet')

        # Removing M2M table for field hashtags on 'Tweet'
        db.delete_table(db.shorten_name(u'timeline_tweet_hashtags'))

        # Removing M2M table for field analysis on 'Tweet'
        db.delete_table(db.shorten_name(u'timeline_tweet_analysis'))

        # Removing M2M table for field url on 'Tweet'
        db.delete_table(db.shorten_name(u'timeline_tweet_url'))

        # Removing M2M table for field image on 'Tweet'
        db.delete_table(db.shorten_name(u'timeline_tweet_image'))


    models = {
        u'timeline.analysis': {
            'Meta': {'object_name': 'Analysis'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '160'})
        },
        u'timeline.hashtag': {
            'Meta': {'object_name': 'Hashtag'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '160'})
        },
        u'timeline.image': {
            'Meta': {'object_name': 'Image'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'image_url': ('django.db.models.fields.URLField', [], {'max_length': '400'})
        },
        u'timeline.tweet': {
            'Meta': {'object_name': 'Tweet'},
            'analysis': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['timeline.Analysis']", 'null': 'True', 'blank': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {}),
            'geo_coordinates': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'hashtags': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['timeline.Hashtag']", 'null': 'True', 'blank': 'True'}),
            'image': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['timeline.Image']", 'null': 'True', 'blank': 'True'}),
            'in_reply_to': ('django.db.models.fields.BigIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'retweet': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'source': ('django.db.models.fields.CharField', [], {'max_length': '400'}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'tweet_id': ('django.db.models.fields.BigIntegerField', [], {'unique': 'True', 'primary_key': 'True'}),
            'url': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['timeline.URL']", 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['timeline.User']"})
        },
        u'timeline.url': {
            'Meta': {'object_name': 'URL'},
            'faviconurl': ('django.db.models.fields.URLField', [], {'default': "''", 'max_length': '1000'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'longurl': ('django.db.models.fields.URLField', [], {'max_length': '1000'}),
            'shorturl': ('django.db.models.fields.URLField', [], {'max_length': '30'}),
            'title': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '1000'})
        },
        u'timeline.user': {
            'Meta': {'object_name': 'User'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'image_url': ('django.db.models.fields.URLField', [], {'max_length': '400'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        }
    }

    complete_apps = ['timeline']