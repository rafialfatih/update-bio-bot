import os
import sys
import time

import tweepy
from dotenv import load_dotenv

load_dotenv()

sys.stdin.reconfigure(encoding='utf-8')
sys.stdout.reconfigure(encoding='utf-8')

consumer_key = os.getenv('CONSUMER_KEY')
consumer_secret = os.getenv('CONSUMER_SECRET_KEY')
access_token = os.getenv('ACCESS_TOKEN')
access_secret_token = os.getenv('ACCESS_SECRET_TOKEN')

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret_token)

api = tweepy.API(auth, wait_on_rate_limit=True)

while True:
    try:
      name = 'rafialfatih'
      tweet_id = '1534527029609017347'

      replies=[]

      for tweet in api.search_tweets(q='to:'+name, result_type='recent'):
          if hasattr(tweet, 'in_reply_to_status_id_str'):
              if (tweet.in_reply_to_status_id_str==tweet_id):
                  replies.append(tweet)

      for reply in replies:
          if reply.id_str not in open('replies_tweet', 'r').read().splitlines():
              open('replies_tweet', 'a').write(reply.id_str+'\n')
              api.update_profile(description=replies[0].text + '\n\n- diperbarui oleh @' + replies[0].user.screen_name)
              print('success')
              time.sleep(30)

          else:
              continue

    except IndexError:
        print('gagal memperbarui profile')
        exit
