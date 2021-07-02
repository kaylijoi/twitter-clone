1. Users
  -> Register
  -> Login
  -> Logout
  -> Profile
    -> Follow
  -> Feed

2. Tweets
  -> Creating
  -> Deleting

3. Following / Followers
  

Database:
python3 manage.py shell
from tweets.models import Tweet
obj = Tweet.objects.create()
Tweet.objects.filter().()