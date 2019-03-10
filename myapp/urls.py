from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^downvote/$', views.downvote, name='downvote'),
    url(r'^downvote-ext/$', views.downvote_ext, name='downvote_ext'),
    url(r'^d/(?P<pid>\d+)/(?P<uid>[\w.+-]+)/$', views.d, name='d'),
    url(r'^s/(?P<pid>\d+)/(?P<uid>[\w.+-]+)/$', views.s, name='s'),
]