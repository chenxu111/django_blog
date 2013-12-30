from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^hello/$',  'article.views.hello', name='hello'),
    # url(r'^hello2/$', 'article.views.hello_template', name='hello_template'),
    # url(r'^hello3/$', 'article.views.hello_from_simple'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', 	include(admin.site.urls)),
    url(r'^articles/',	include('article.urls')),

    url(r'^accounts/login/$','django_test.views.login'),
    url(r'^accounts/auth/$','django_test.views.auth_view'),
    url(r'^accounts/logout/$','django_test.views.logout'),
    url(r'^accounts/loggedin/$','django_test.views.loggedin'),
    url(r'^accounts/invalid/$','django_test.views.invalid_login'),

    url(r'^accounts/register/$','django_test.views.register_user'),
    url(r'^accounts/register_success/$','django_test.views.register_success'),
    
)