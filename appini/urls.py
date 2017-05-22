"""
Este codigo es lo mismo que el de abajo

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]

"""

import django.conf.urls
from . import views

urlpatterns = [
    django.conf.urls.url(r'^$', views.index, name='index'),
    django.conf.urls.url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    django.conf.urls.url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    django.conf.urls.url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]
