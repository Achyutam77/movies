#from django.contrib import admin

# Register your models here.
#from .models import Recommendation

#@admin.register(Recommendation)
#class RecommendationAdmin(admin.ModelAdmin):
#    list_display = ['user', 'movie', 'Recommended_at']

from django.contrib import admin
from .models import Recommendation

admin.site.register(Recommendation)