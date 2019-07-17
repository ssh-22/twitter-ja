from django.shortcuts import render, get_object_or_404, redirect
from django.conf import settings

from django.views.generic import View, CreateView
from django.views.generic.list import ListView
from timeline.models import Tweet, Favorite
from accounts.models import Account, Relationship
from django.contrib.auth.models import User

from .forms import TweetForm
from django.urls import reverse_lazy
from django.http import JsonResponse

import uuid
from django.db.models import Q

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

class TimelineList(LoginRequiredMixin, View):
    def get(self, request):
        template_name = 'timeline/index.html'
        ordered_tweets = Tweet.objects.all().order_by('-created_at')

        if self.request.user:
            current_user = self.request.user
            try:
                following_tweets = [i for i in Tweet.objects.filter(Q(user_id__follower__following_id=request.user.user) | Q(user_id=request.user.user)).order_by('-created_at').distinct()]
                account_of_tweets = [following_tweet.user_id for following_tweet in following_tweets]
                user_of_tweets = [account_of_tweet.user for account_of_tweet in account_of_tweets]

                current_account_of_user = current_user.user
                current_tweet_of_user = current_account_of_user.user_ids.all().order_by('-created_at')
                is_favorited = [following_tweet.tweet_ids.filter(user_id=self.request.user.user) for following_tweet in following_tweets]
                context = zip(following_tweets, user_of_tweets, account_of_tweets, is_favorited)

                len_of_context = 4

            except Account.DoesNotExist:
                current_account_of_user = None
                current_tweet_of_user = None
                account_of_tweets = [ordered_tweet.user_id for ordered_tweet in ordered_tweets]
                user_of_tweets = [account_of_tweet.user for account_of_tweet in account_of_tweets]

                context = zip(ordered_tweets, user_of_tweets, account_of_tweets)
                len_of_context = 3

                Account.objects.create(user=request.user, profile='', name='匿名希望')

        else:
            current_user = None
            current_account_of_user = None
            current_tweet_of_user = None
            is_favorited = None

            context = zip(ordered_tweets, user_of_tweets, account_of_tweets)
            len_of_context = 3

        return render(request, template_name, 
        {'context': context, 
        'current_user': current_user, 
        'current_account_of_user': current_account_of_user, 
        'len_of_context': len_of_context,
        }
        )

@login_required
def tweet_add(request):
    tweet = request.POST.get('tweet')
    picture = request.FILES.get('picture')
    user_id = request.user.user
    Tweet.objects.create(tweet=tweet, picture=picture, user_id=user_id)

    return redirect('timeline:index')

@login_required
def tweet_delete(request):
    tweet = request.POST.get('tweet')
    Tweet.objects.filter(id=uuid.UUID(tweet)).delete()
    return redirect('timeline:index')

@login_required
def favorite_add(request):
    tweet = request.POST.get('tweet')
    tweet_id = Tweet.objects.get(id=uuid.UUID(tweet))
    user_id = request.user.user
    Favorite.objects.create(tweet_id=tweet_id, user_id=user_id)

    return redirect('timeline:index')

@login_required
def favorite_delete(request):
    tweet = request.POST.get('tweet')
    tweet_id = Tweet.objects.get(id=uuid.UUID(tweet))
    user_id = request.user.user
    Favorite.objects.filter(tweet_id=tweet_id, user_id=user_id).delete()

    return redirect('timeline:index')

class SearchList(LoginRequiredMixin, View):
    def get(self, request):
        template_name = 'timeline/search.html'
        accounts = Account.objects.all().exclude(user=request.user)
        user_of_accounts = [_.user for _ in accounts]

        context = zip(accounts, user_of_accounts)

        return render(request, template_name,
        {'context': context})