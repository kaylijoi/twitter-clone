from django.http.response import Http404
from django.shortcuts import render
from django.http import HttpResponse
from .models import Tweet

# Create your views here.
def home_view(request, *args, **kwargs):
  return HttpResponse("<h1>Hello world</h1>")

def tweet_detail_view(request, tweet_id, *args, **kwargs):
  try:
    obj = Tweet.objects.get(id=tweet_id)
  except:
    raise Http404
  return HttpResponse(f"<h1>Tweet id: {tweet_id} - {obj.content}</h1>")