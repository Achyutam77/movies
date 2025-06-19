from django.contrib import admin

# Register your models here.
from .models import Favorites, WatchHistory

@admin.register(Favorites)
class FavoritesAdmin(admin.ModelAdmin):
    list_display = ['user', 'movie', 'added_at']

@admin.register(WatchHistory)
class WatchHistoryAdmin(admin.ModelAdmin):
    list_display = ['user', 'movie', 'watched_at']
