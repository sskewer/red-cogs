import tweepy
import requests

import discord
from contextlib import suppress
from redbot.core import commands

BaseCog = getattr(commands, "Cog", object)


# REMEMBER TO SET PARAMETERS BELOW USING THIS COMMAND
# [p]set api TweetRepost webhook_url,XXXXX consumer_key,XXXXX consumer_secret,XXXXX access_token,XXXXX access_token_secret,XXXXX

# REMEMBER TO CHANGE THIS USER ACCORDING TO YOUR NEEDS
tweet_user = "FortniteStatus" 


class TweetRepost(BaseCog):
  
  def __init__(self, bot):
    self.bot = bot
        
  @commands.Cog.listener()
  async def on_message(self, message):
    try:
      api_tokens = await bot.get_shared_api_tokens('TweetRepost')
    except:
      return
    auth = tweepy.OAuth1UserHandler(
      api_tokens["consumer_key"], 
      api_tokens["consumer_secret"], 
      api_tokens["access_token"], 
      api_tokens["access_token_secret"]
    )
    api = tweepy.API(auth)
    tweets = api.search_tweets(f"from:{str(tweet_user)}", count = 5, tweet_mode = "extended")
    to_post = []
    for tweet in tweets:
      # Getting tweet data
      input_data = tweet._json
      # Getting image
      try:
        image = input_data["entities"]["media"][0]["media_url"]
      except IndexError:
        image = None
      # Extracting important data
      to_post.append({
        "id": tweet.id,
        "text": input_data["full_text"],
        "image": image,
        "timestamp": input_data["created_at"],
      })
    # Webhook Posts
    for post in to_post:
      try:
        requests.post(
          "https://Fortnite.mettiushyper.repl.co/webhook",
          headers = {
            "webhook_url": api_tokens["webhook_url"],
          },
          json = {
            "text": post["text"],
            "image": post["image"],
            "timestamp": post["timestamp"],
            "color": "#ffffff",
            "translate_language": "it",
          },
        )
      except:
        pass


def setup(bot):
  bot.add_cog(TweetRepost(bot))
