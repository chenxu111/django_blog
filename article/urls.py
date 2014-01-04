from django.conf.urls import patterns,include,url

urlpatterns = patterns('article',
	url(r'^hello/$',  'views.hello', name='hello'),
	url(r'^hello2/$', 'views.hello_template', name='hello_template'),
 	url(r'^hello3/$', 'views.hello_from_simple'),
	url(r'^all/$','views.articles'),
	url(r'^get/(?P<article_id>\d+)/$','views.article'),
	url(r'^create/$','views.create'),
	url(r'^language/(?P<language>[a-z\-]+)/$','views.language'),
	url(r'^like/(?P<article_id>\d+)/$','views.like_article'),
	url(r'^unlike/(?P<article_id>\d+)/$','views.unlike_article'),
)