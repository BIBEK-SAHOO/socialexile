from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^downvote/$', views.downvote, name='downvote'),
    url(r'^downvote-ext/$', views.downvote_ext, name='downvote_ext'),
    url(r'^d/(?P<pid>[0-9]+)/(?P<uid>\w+)/$', views.d, name='d'),
    url(r'^api/downvote/$', views.DownVoteAPI.as_view()),
    url(r'^api/downvote-ext/$', views.DownVoteExtAPI.as_view()),
]