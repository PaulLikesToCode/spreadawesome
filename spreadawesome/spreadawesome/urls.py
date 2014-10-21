from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework import routers
from chucknorris.api.serializers import TweetSerializer, TweetViewSet
from chucknorris.views.views import Index, SendTweet

router = routers.DefaultRouter()
router.register(r'tweets', TweetViewSet)

admin.autodiscover()

urlpatterns = patterns('chucknorris.views.views',
    # Examples:
    # url(r'^$', 'spreadawesome.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^test/', 'test', name='test'),
    url(r'^login/?$', "login", name="twitter_login"),
    url(r'^logout_twitter/?$', "logout_twitter", name="twitter_logout"),
    url(r'^thanks?$', "thanks", name="twitter_callback"),
    url(r'^send_tweet/?$', SendTweet.as_view(), name="send_tweet"),
    url(r'^$', Index.as_view(), name='index'),
    # url(r'^tweets/(?P<pk>[0-9]+)/$', 'views.tweet_detail'),
    # url(r'^$', 'index', name='index'),
    # url(r'^send_tweet/?$', 'send_tweet', name="send_tweet"),
	# url(r'^', include(router.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

)
