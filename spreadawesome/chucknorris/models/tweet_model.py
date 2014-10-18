from django.db import models
from quote_model import Quote
from django.contrib.auth.models import User
# from django.utils import timezone
import datetime

# class TweetManager(models.Manager):
# 	def save(self, user_id, receipent_handle, quote_id=None, tweet_text, post_timestamp=None):
# 		if post_timestamp == None:
# 			post_timestamp = datetime.now
# 			print post_timestamp
# 		self.create(user_id=user_id, receipent_handle=receipent_handle, quote_id=quote_id, tweet_text=tweet_text, post_timestamp=post_timestamp)
# 		return self


class Tweet(models.Model):
	user_id = models.ForeignKey(User)
	receipent_handle = models.CharField(max_length=100, null=True, blank=True)
	quote_id = models.ForeignKey('Quote', null=True, blank=True)
	tweet_text = models.TextField(null=True)
	post_timestamp = models.DateTimeField(default=datetime.datetime.now)
	# objects = TweetManager()
	class Meta: 
		app_label = "chucknorris"

