# Create your views here.

from django.shortcuts import render_to_response
from timeline.models import Tweet
from timeline.models import User
from django.http import Http404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Count
from django.template.context import RequestContext

def start(request):
	return render_to_response(
			'index.html',
		)

def timeline(request):
	#timeline_list = Tweet.objects.all().order_by('created_at')
	timeline_list = Tweet.objects.filter(retweet=False).order_by('created_at')
	tweets = len(timeline_list)
	paginator = Paginator(timeline_list, 25)

	page = request.GET.get('page')
	try:
		timeline = paginator.page(page)
	except PageNotAnInteger:
		timeline = paginator.page(1)
	except EmptyPage:
		timeline = paginator.page(paginator.num_pages)

	return render_to_response(
			'timeline/index.html',
			{'timeline': timeline, 'tweets': tweets},
			context_instance=RequestContext(request)
		)

def user(request, id):
	try:
		u = User.objects.get(pk=id)
		t = Tweet.objects.filter(user__id=id).order_by('created_at')
	except User.DoesNotExist:
		raise Http404
	return render_to_response(
			'user/index.html',
			{'user': u, 'tweets': t, 'num_tweets': len(t)},
			context_instance=RequestContext(request)
		)

def tweet(request, tweet_id):
	try:
		t = Tweet.objects.get(pk=tweet_id)
	except Tweet.DoesNotExist:
		return render_to_response(
				'tweet/unbekannt.html',
				{'tweet': tweet_id},
			)
	return render_to_response(
			'tweet/index.html',
			{'tweet': t},
			context_instance=RequestContext(request)
		)

def zufall(request):
	import random
	tweets = Tweet.objects.all().count()
	random_tweet = random.random() * (tweets - 1)
	try:
		t = Tweets.objects.all()[slice: random_tweet+1]
	except Tweet.DoesNotExist:
		return render_to_response(
				'tweet/unbekannt.html',
				{'tweet': tweet_id},
			)
	return render_to_response(
			'zufall/index.html',
			{'tweet': t},
			context_instance=RequestContext(request)
		)
