from django.conf.urls import patterns, url
from testapp.views import *

urlpatterns = patterns('',
    url(r'^$', manage_articles, name='formsets'),
)
