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
		t_list = Tweet.objects.filter(user__id=id).order_by('created_at')
		tweets = len(t_list)
		paginator = Paginator(t_list, 25)
		page = request.GET.get('page')
		try:
			t = paginator.page(page)
		except PageNotAnInteger:
			t = paginator.page(1)
		except EmptyPage:
			t = paginator.page(paginator.num_pages)

	except User.DoesNotExist:
		raise Http404
	return render_to_response(
			'user/index.html',
			{'user': u, 'timeline': t, 'tweets': tweets},
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
		t = Tweet.objects.all()[random_tweet:random_tweet+1]
	except Tweet.DoesNotExist:
		raise Http404
	return render_to_response(
			'zufall/index.html',
			{'tweets': t},
			context_instance=RequestContext(request)
		)

def bilder(request):
	timeline_list = Tweet.objects.filter(retweet=False,image__isnull=False).order_by('created_at')
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
			'bilder/index.html',
			{'timeline': timeline, 'tweets': tweets},
			context_instance=RequestContext(request)
		)

def links(request):
	timeline_list = Tweet.objects.filter(retweet=False,url__isnull=False).order_by('created_at')
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
			'links/index.html',
			{'timeline': timeline, 'tweets': tweets},
			context_instance=RequestContext(request)
		)

