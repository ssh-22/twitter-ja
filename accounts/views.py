from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.conf import settings

from django.views.generic import View
from django.views.generic.list import ListView
from timeline.models import Tweet, Favorite
from accounts.models import Account, Relationship
from django.contrib.auth.models import User

import uuid as _uuid
from django.db import IntegrityError

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

class AccountDetailView(LoginRequiredMixin, View):
    def get(self, request, username=None):
        template_name = 'accounts/index.html'
        target_user = User.objects.get(username=username)

        try:
            account_of_user = target_user.user
            tweets_of_user = account_of_user.user_ids.all().order_by('-created_at')
            
            # usernameのユーザーがフォローしている数
            total_following = account_of_user.following.count()
            # usernameのユーザーがフォローされている数
            total_follower = account_of_user.follower.count()

            # ログインユーザーがusernameのユーザーをフォローしているか
            is_following = account_of_user.follower.filter(following_id=request.user.user)
        
        except (IntegrityError, Account.DoesNotExist):
            Account.objects.create(user=request.user, profile='', name='匿名希望')

            account_of_user = target_user.user
            tweets_of_user = account_of_user.user_ids.all().order_by('-created_at')
            
            # usernameのユーザーがフォローしている数
            total_following = None

            # usernameのユーザーがフォローされている数
            total_follower = None

            # ログインユーザーがusernameのユーザーをフォローしているか
            is_following = None

        return render(request, template_name, 
        {'target_user': target_user, 
        'account_of_user': account_of_user, 
        'tweets_of_user': tweets_of_user, 
        'total_following': total_following, 
        'total_follower': total_follower,
        'is_following': is_following}
        )

@login_required
def follow(request, username=None):
    following_id = request.user.user
    follower_id = User.objects.get(username=username).user
    Relationship.objects.create(following_id=following_id, follower_id=follower_id)

    return redirect('accounts:detail', username)

@login_required
def unfollow(request, username=None):
    following_id = request.user.user
    follower_id = User.objects.get(username=username).user
    Relationship.objects.filter(following_id=following_id, follower_id=follower_id).delete()

    return redirect('accounts:detail', username)

@login_required
def edit(request, username=None):
    account_user = request.user
    account = Account.objects.get(user=account_user)
    account.profile = request.POST.get('profile')
    account.name = request.POST.get('name')

    account.background_image = request.FILES.get('background_image', False)    
    account.profile_image = request.FILES.get('profile_image', False)

    if account.background_image is False:
        account.background_image = Account.objects.get(user=account_user).background_image
    
    if account.profile_image is False:
        account.profile_image = Account.objects.get(user=account_user).profile_image

    account.save()

    return redirect('accounts:detail', username)