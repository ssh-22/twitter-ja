from django.contrib import admin

from .models import Tweet, Favorite

# Tweetモデルを登録する
@admin.register(Tweet)
class AdminTweet(admin.ModelAdmin):
    pass

# Favoriteモデルを登録する
@admin.register(Favorite)
class AdminFavorite(admin.ModelAdmin):
    pass