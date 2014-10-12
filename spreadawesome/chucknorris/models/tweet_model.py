from django.db import models
from quote_model import Quote
from django.contrib.auth.models import User


class Tweet(models.Model):
	user_id = models.ForeignKey(User)
	receipent_handle = models.CharField(max_length=100, null=True, blank=True)
	quote_id = models.ForeignKey(Quote, null=True)
	tweet_text = models.TextField(null=True)
	post_timestamp = models.DateTimeField(null=True)

	class Meta: 
		app_label = "chucknorris"