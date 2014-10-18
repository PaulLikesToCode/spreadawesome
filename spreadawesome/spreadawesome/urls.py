from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework import routers
from chucknorris.api.serializers import TweetSerializer, TweetViewSet

router = routers.DefaultRouter()
router.register(r'tweets', TweetViewSet)

admin.autodiscover()

urlpatterns = patterns('chucknorris.views',
    # Examples:
    # url(r'^$', 'spreadawesome.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^test/', 'views.test', name='test'),
    url(r'^login/?$', "views.login", name="twitter_login"),
    url(r'^logout_twitter/?$', "views.logout_twitter", name="twitter_logout"),
    url(r'^thanks?$', "views.thanks", name="twitter_callback"),
    url(r'^send_tweet/?$', 'views.send_tweet', name="send_tweet"),
    # url(r'^tweets/$', 'views.tweet_list'),
    # url(r'^tweets/(?P<pk>[0-9]+)/$', 'views.tweet_detail'),
    url(r'^$', 'views.index', name='index'),
	# url(r'^', include(router.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

)
