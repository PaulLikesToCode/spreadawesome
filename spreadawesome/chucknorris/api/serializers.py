from rest_framework import serializers, viewsets
from ..models.tweet_model import Tweet 
from django.contrib.auth.models import User
from ..models.user_model import TwitterInfo

class TweetSerializer(serializers.ModelSerializer):
	class Meta: 
		model = Tweet
		fields = ('quote_id', 'tweet_text')

class TweetViewSet(viewsets.ModelViewSet):
	queryset = Tweet.objects.all()
	serializer_class = TweetSerializer

