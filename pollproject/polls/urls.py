from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index),
    #    url(r'^students/$', views.student),
    url(r'(?P<candidate_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'(?P<candidate_id>[0-9]+)/result/$', views.result, name='result'),
    url(r'(?P<candidate_id>[0-9]+)/vote/$', views.vote, name='vote'),
]
