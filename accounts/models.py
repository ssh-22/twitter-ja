from django.db import models
from django.contrib.auth.models import User

import uuid

class Account(models.Model):
    """
    既存の User モデルを拡張する(OneToOneFieldを追加)
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user')
    uuid = models.UUIDField(default=uuid.uuid4,
                            primary_key=True, editable=False, verbose_name='ユーザID')
    profile = models.TextField(blank=True, verbose_name='プロフィール')
    background_image = models.ImageField(verbose_name='背景画像', default='twitter.jpg')
    profile_image = models.ImageField(verbose_name='プロフィール画像', default='egg.jpg')
    # total_following = models.IntegerField(verbose_name='フォロー数')
    # total_followers = models.IntegerField(verbose_name='フォローワー数')
    name = models.CharField(max_length=255, verbose_name='名前')

    def __str__(self):
        return str(self.uuid)

class Relationship(models.Model):
    """
    Relationshipモデル
    """
    following_id = models.ForeignKey(Account, verbose_name='フォローID', related_name='following', on_delete=models.CASCADE)
    follower_id = models.ForeignKey(Account, verbose_name='フォローワーID', related_name='follower', on_delete=models.CASCADE)
    # user_id = models.ForeignKey(Account, verbose_name='ユーザーID', on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True, verbose_name='更新日時')

    class Meta:
        unique_together = ('following_id', 'follower_id')
    
    # def __str__(self):
    #     template = '{0.following_id} {0.follower_id}'
    #     return template.format(self)