from django.shortcuts import render, redirect
from django.template.context import RequestContext
from django.conf import settings
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.models import User 
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from ..models.tweet_model import Tweet 
from ..api.serializers import TweetSerializer
import datetime

from twython import Twython 
from ..models.user_model import TwitterInfo

def check_user_status(request):
	try: 
		final_oauth_token = request.session['final_step']['oauth_token']
		final_token_secret = request.session['final_step']['oauth_token_secret']
		twitter = Twython(settings.TWITTER_KEY, settings.TWITTER_SECRET, final_oauth_token, final_token_secret)
		tweeter = twitter.verify_credentials()
		if tweeter is not None:
			return tweeter
		else:
			return False
	except:
		return False


def index(request):
	try:
		user = User.objects.get(username=request.session['screen_name'])
		data = {'user': user, 
			'user_icon':request.session['profile_image_url'],
			'oauth_token': request.session['final_step']['oauth_token'],
			'oauth_token_secret': request.session['final_step']['oauth_token_secret']
			}
	except:
		data = {}
	return render(request, 'index.html', data)

def test(request):
	context = RequestContext(request, {'user': request.user})
	return render(request, 'test.html', context_instance=context)



def login(request):
	twitter = Twython(settings.TWITTER_KEY, settings.TWITTER_SECRET)
	auth = twitter.get_authentication_tokens(callback_url='http://localhost:8000/thanks')
	request.session['oauth_token'] = auth['oauth_token']
	request.session['oauth_token_secret'] = auth['oauth_token_secret']
	# request.session['request_token'] = auth_props
	return HttpResponseRedirect(auth['auth_url'])

def thanks(request):
	# We need these variables
	oauth_verifier = request.GET['oauth_verifier']
	oauth_token = request.session['oauth_token']
	oauth_secret = request.session['oauth_token_secret']
	# Get the first part of authentication
	twitter = Twython(settings.TWITTER_KEY, settings.TWITTER_SECRET, oauth_token, oauth_secret)
	request.session['final_step'] = twitter.get_authorized_tokens(oauth_verifier)
	final_oauth_token = request.session['final_step']['oauth_token']
	final_token_secret = request.session['final_step']['oauth_token_secret']
	#Get the second part of authentication
	twitter = Twython(settings.TWITTER_KEY, settings.TWITTER_SECRET, final_oauth_token, final_token_secret)
	twitter_user = twitter.verify_credentials()
	request.session['screen_name'] = twitter_user['screen_name']
	request.session['profile_image_url'] = twitter_user['profile_image_url']
	TwitterInfo.objects.get_or_save(twitter_user['screen_name'], oauth_token, oauth_secret)
	# data = {
	# 	'screen_name': twitter_user['screen_name'],
	# 	'profile_image_url': twitter_user['profile_image_url']
	# }
	# print twitter.show_user(screen_name = account_name)
	return redirect('index')

def logout_twitter(request):
	logout(request)
	return redirect(index)


@csrf_exempt
def send_tweet(request):
	if request.method == 'POST':
		data = JSONParser().parse(request)
		user = User.objects.get(username=data['twitter_handle'])
		try:
			twitter_message = Tweet(user_id=user, receipent_handle=data['twitter_handle'], tweet_text=data['message'])
			twitter_message.save()
			message = "Thanks for spreading awesomeness!"
		except:
			message = "Sorry"
		return JsonResponse({'message': message})

		# end test area

		# twitter = Twython(settings.TWITTER_KEY, settings.TWITTER_SECRET, data['oauth_token'], data['oauth_token_secret'])
		# try:
		# 	# twitter.update_status(status=data['message'])
		# 	twitter_message = Tweet(user_id=user.id, receipent_handle=data['twitter_handle'], tweet_text=data['message'], post_timestamp=datetime.now())
		# 	print 'trying'
		# 	print twitter_message
		# 	twitter_message.save()
		# 	return JsonResponse({'message': "cool"})
		# except:
		# 	print 'sorry'
		# 	return JsonResponse({'message': 'not cool'})


@csrf_exempt
def tweet_list(request):
	# if check_user_status(request) 
	if request.method == 'GET': 
		user_status = check_user_status(request)
		if user_status is not False:
			user = User.objects.get(username=user_status['screen_name'])
			tweets = Tweet.objects.filter(user_id = user.id)
			serializer = TweetSerializer(tweets, many=True)
			return JsonResponse(serializer.data, safe=False)
		else:
			return HttpResponse('You are not allowed to do this. You are not a user')

	elif request.method == 'POST':
		data = JSONParser().parse(request)
		serializer = TweetSerializer(data=data)
		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data, status=201, safe=False)
		return JsonResponse(serializer.errors, status=400, safe=False)

@csrf_exempt
def tweet_detail(request, pk):
	try: 
		tweet = Tweet.objects.get(pk=pk)
	except Tweet.DoesNotExist:
		return HttpResponse(status = 404)

	if request.method == 'GET':
		serializer = TweetSerializer(tweet)
		return JsonResponse(serializer.data, safe=False)
	elif request.method == 'PUT':
		data = JSONParser().parse(request)
		serializer = TweetSerializer(tweet, data=data)
		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data, safe=False)
		return JsonResponse(serializer.errors, status=400, safe=False8)
	elif request.method == 'DELETE':
		snippet.delete()
		return HttpResponse(status=204)


"""
I want to refactor this code into class based generic views. This area will be devoted to that effort. 
Right now I'm still using functional views. 

Login should be a base class, thanks should inherit from Login. 


"""


















