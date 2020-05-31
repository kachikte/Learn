from django.urls import path
from django.conf.urls import url
from . import views



urlpatterns = [
	path('', views.index, name='index'),
    url(r'^topics/$', views.topics, name='topics'),
    url(r'^topic/(?P<topic_id>\d+)/$', views.topic, name='topic'),
]