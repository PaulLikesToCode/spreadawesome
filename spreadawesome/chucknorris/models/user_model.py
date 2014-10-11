from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class TwitterInfo(models.Model):
	user = models.OneToOneField(User)
	twitter_handle = models.CharField(max_length = 100)

	class Meta: 
		app_label = "chucknorris"
