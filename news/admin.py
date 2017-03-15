from __future__ import unicode_literals
from django.contrib import admin
from .models import Feed, Article, Story

# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'feed','political_spectrum','story' )
    save_on_top = True


class StoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'publication_date','description')

admin.site.register(Feed)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Story, StoryAdmin)
