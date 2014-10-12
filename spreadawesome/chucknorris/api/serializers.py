from rest_framework import serializers, viewsets
from ..models.tweet_model import Tweet 

class TweetSerializer(serializers.ModelSerializer):
	class Meta: 
		model = Tweet
		fields = ('quote_id', 'tweet_text')

class TweetViewSet(viewsets.ModelViewSet):
	queryset = Tweet.objects.all()
	serializer_class = TweetSerializer