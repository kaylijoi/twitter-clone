from django import forms
from .models import Tweet

MAX_TWEET_LENGTH = 240

class TweetForm(forms.ModelForm):
  # Describing entire form itself (meta)
  class Meta:
    model = Tweet
    fields = ['content']

    # Make sure form is under the char limit
    def clean_content(self):
      content = self.cleaned_data.get("content")
      if len(content) > MAX_TWEET_LENGTH:
        raise forms.ValidationError("Exceeded character limit")
      return content
