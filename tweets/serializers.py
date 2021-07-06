from django.conf import settings
from rest_framework import serializers
from .models import Tweet

MAX_TWEET_LENGTH = settings.MAX_TWEET_LENGTH

class TweetSerializer(serializers.ModelSerializer):
  class Meta:
    model = Tweet
    fields = ['user', 'id', 'content', 'likes', 'timestamp']

    def validate_content(self, value):
      if len(value) > MAX_TWEET_LENGTH:
        raise serializers.ValidationError("Exceeded character limit")
      return value

# Translates django modesl into other formats - allows complex data to be converted to native python datatypes for rendering to JSON/XML