from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('accounts.views',
    url(r'^$', 'home'),
)

urlpatterns += patterns('',
    url(r'^login/$', 'django.contrib.auth.views.login', {
        'template_name': 'accounts/login.html'
    }, name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {
        'template_name': 'accounts/logged_out.html'
    }, name='logout'),
    url(r'^password_change/$', 'django.contrib.auth.views.password_change', {
        'template_name': 'accounts/password_change_form.html'
    }, name='password_change'),
    url(r'^password_change/done/$', 'django.contrib.auth.views.password_change_done', {
        'template_name': 'accounts/password_change_done.html'
    }, name='password_change_done'),
)
