from django.db import models



class ArticleManager(models.Manager):
    def storied(self):
        return self.get_queryset().filter(story=True)
# Create your models here.

class Feed(models.Model):
    title = models.CharField(max_length=200, default= "news")
    url = models.URLField()
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Story(models.Model):
    title = models.CharField(max_length=200, default= "")
    description = models.TextField()
    publication_date = models.DateTimeField()
    
    def __str__(self):
        return self.title
  

class Article(models.Model):
    feed = models.ForeignKey(Feed)
    title = models.CharField(max_length=200)
    url = models.URLField()
    grouped = models.BooleanField(default=False)
    political_spectrum = models.CharField(max_length=20, default= "none")
    publication_date = models.DateTimeField()
    description = models.TextField(null=True, default=None, blank=True)
    objects= ArticleManager()
    story = models.ForeignKey(Story, null=True, default=None, blank=True)

    def __str__(self):
        return self.title


