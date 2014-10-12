from django.contrib import admin
from chucknorris.models.tweet_model import Tweet 
from chucknorris.models.quote_model import Quote 
from chucknorris.models.user_model import TwitterInfo

admin.site.register(Tweet)
admin.site.register(Quote)
admin.site.register(TwitterInfo)

# Register your models here.
