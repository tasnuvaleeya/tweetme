from django.conf.urls import url
# from .views import TweetDetailView, TweetListView,TweetCreateView,TweetUpdateView,TweetDeleteView
from django.views.generic.base import RedirectView
from .views import TweetListAPIView, TweetCreateAPIView, RetweetAPIView

urlpatterns = [

    url(r'^$', TweetListAPIView.as_view(),name='list'),                 # /api/tweet/
    url(r'^create/', TweetCreateAPIView.as_view(), name='create'),       # /api/tweet/create/
    url(r'^(?P<pk>\d+)/retweet/$', RetweetAPIView.as_view(), name='retweet'),      # /api/tweet/id/retweet/

]