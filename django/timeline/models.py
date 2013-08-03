from django.db import models

# Create your models here.

class User(models.Model):
	name = models.CharField(max_length=20)
	image_url = models.URLField(max_length=400)
	image = models.ImageField(upload_to='profile')

	def get_details(self):
		return [(field.name, field.value_to_string(self)) for field in User._meta.fields]

	def __unicode__(self):
		return self.name

class Hashtag(models.Model):
	name = models.CharField(max_length=160)

class Analysis(models.Model):
	name = models.CharField(max_length=160)

class URL(models.Model):
	shorturl = models.URLField(max_length=30)
	longurl = models.URLField(max_length=1000)
	faviconurl = models.URLField(max_length=1000, default='')
	title = models.CharField(max_length=1000, default='')

	def __unicode__(self):
		return self.longurl

class Image(models.Model):
	image = models.ImageField(upload_to='images')
	image_url = models.URLField(max_length=400)

	def __unicode__(self):
		return self.image

class Tweet(models.Model):
	tweet_id = models.BigIntegerField(primary_key=True,unique=True)
	user = models.ForeignKey(User)
	created_at = models.DateTimeField()
	text = models.CharField(max_length=200)
	source = models.CharField(max_length=400)
	in_reply_to = models.BigIntegerField(null=True,blank=True)
	geo_coordinates = models.CharField(max_length=200,null=True,blank=True)
	hashtags = models.ManyToManyField(Hashtag,null=True,blank=True)
	retweet = models.BooleanField()
	analysis = models.ManyToManyField(Analysis,null=True,blank=True)
	url = models.ManyToManyField(URL,null=True,blank=True)
	image = models.ManyToManyField(Image,null=True,blank=True)
	
	def get_details(self):
		return [(field.name, field.value_to_string(self)) for field in Tweet._meta.fields]

	def __unicode__(self):
		return u"%s %s" % (self.user, self.text)

