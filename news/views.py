from django.shortcuts import render
from .models import Article, Feed

# Create your views here.

def articles_list(request):
    return render(request, 'news/articles_list.html', {})
