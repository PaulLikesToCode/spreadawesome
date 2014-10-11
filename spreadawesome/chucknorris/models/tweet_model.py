from django.db import models
from quote_model import Quote
from django.contrib.auth.models import User


class Tweet(models.Model):
	user_id = models.ForeignKey(User)
	receipent_handle = models.CharField(max_length=100, null=True)
	quote_id = models.ForeignKey(Quote)
	models.DateTimeField(null=True)

	class Meta: 
		app_label = "chucknorris"