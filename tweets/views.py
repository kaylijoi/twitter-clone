import random
from django.conf import settings
from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, JsonResponse
from django.utils.http import is_safe_url
from rest_framework import serializers
from rest_framework.response import Response

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .forms import TweetForm
from .models import Tweet
from .serializers import TweetSerializer
ALLOWED_HOSTS = settings.ALLOWED_HOSTS

# Create your views here.
def home_view(request, *args, **kwargs):
  return render(request, "pages/home.html", context={}, status=200)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def tweet_create_view(request, *args, **kwargs):
  serializer = TweetSerializer(data = request.POST)
  if serializer.is_valid():
    serializer.save(user=request.user)
    return Response(serializer.data, status=201)
  return Response({}, status=400)


@api_view(['GET'])
def tweet_list_view(request, *args, **kwargs):
  qs = Tweet.objects.all()
  serializer = TweetSerializer(qs, many=True)
  return Response(serializer.data, status=200)


@api_view(['GET'])
def tweet_detail_view(request, tweet_id, *args, **kwargs):
  qs = Tweet.objects.filter(id=tweet_id)
  if not qs.exists():
    return Response({}, status=404)
  obj = qs.first()
  serializer = TweetSerializer(obj)
  return Response(serializer.data, status=200)

