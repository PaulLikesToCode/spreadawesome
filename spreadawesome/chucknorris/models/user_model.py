from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class TwitterInfoManager(models.Manager):
	def get_or_save(self, twitter_handle, oauth_token, oauth_secret):
		if User.objects.filter(username=twitter_handle).exists():
			user = User.objects.get(username = twitter_handle)
			return self.filter(user=user)
		else:
			user = User.objects.create_user(twitter_handle)
			twitter_user = self.create(user=user, oauth_token=oauth_token, oauth_secret=oauth_secret)
			return twitter_user

class TwitterInfo(models.Model):
	user = models.OneToOneField(User)
	oauth_token = models.CharField(max_length=200, null=True)
	oauth_secret = models.CharField(max_length=200, null=True)

	objects = TwitterInfoManager()

	def __unicode__(self):
		return "{0}".format(self.user)

	class Meta: 
		app_label = "chucknorris"
