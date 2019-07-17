from django.db import models
from accounts.models import Account

import uuid

class Tweet(models.Model):
    """
    Tweetモデル
    """
    user_id = models.ForeignKey(Account, verbose_name='ユーザーID', on_delete=models.CASCADE, related_name='user_ids')
    id = models.UUIDField(default=uuid.uuid4,
                            primary_key=True, editable=False, verbose_name='ツイートID')
    tweet = models.TextField(verbose_name='ツイート')
    picture = models.ImageField(verbose_name='ツイート画像', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='投稿日時')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='更新日時')

    def __str__(self):
        return str(self.id)
    
class Favorite(models.Model):
    """
    Favoriteモデル
    """
    user_id = models.ForeignKey(Account, verbose_name='ユーザーID', on_delete=models.CASCADE, related_name='account_ids')
    tweet_id = models.ForeignKey(Tweet, verbose_name='ツイートID', on_delete=models.CASCADE, related_name='tweet_ids')
    id = models.UUIDField(default=uuid.uuid4,
                            primary_key=True, editable=False, verbose_name='いいねID')
    created_at = models.DateTimeField(auto_now=True, verbose_name='更新日時')

    def __str__(self):
        return str(self.id)