from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'aufschrei.views.home', name='home'),
    # url(r'^aufschrei/', include('aufschrei.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^timeline/$', 'timeline.views.timeline'),
    url(r'^user/(?P<id>\d+)/$', 'timeline.views.user'),
    url(r'^tweet/(?P<tweet_id>\d+)/$', 'timeline.views.tweet'),
)

if settings.DEBUG:
	urlpatterns += patterns('',
			url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
				'document_root': settings.MEDIA_ROOT,
			}),
			url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {
				'document_root': settings.STATIC_ROOT,
			}),
	)

