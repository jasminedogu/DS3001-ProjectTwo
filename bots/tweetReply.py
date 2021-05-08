#!/usr/bin/env python
# tweepy-bots/bots/autoreply.py

import tweepy
import logging
#from config import create_api
import time
import os


twitter_keys = {
        'consumer_key':        '9H3SSelJkpQNs7XJm60f3E0wW',
        'consumer_secret':     'LKPJjaU3p9meQZzfADgPD2ef1AmkWi5PpTROIxI7008Z6CvsWg',
        'access_token_key':    '1391110880297984005-IuJ0IOY811bpZb8ZXeTzb3Ysb5xv4S',
        'access_token_secret': 'lRSwpkyDnPC1saOq4HkIT3HePs7T6BXByeElLjPf84L5E'
    }

#Setup access to API
auth = tweepy.OAuthHandler(twitter_keys['consumer_key'], twitter_keys['consumer_secret'])
auth.set_access_token(twitter_keys['access_token_key'], twitter_keys['access_token_secret'])

api = tweepy.API(auth)



logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


def createPic(text, author):
    os.system("python3 quotesmaker.py -q \" " + text + " \" -a \" " + author +" \"   " )      
    

def check_mentions(api, since_id):
    logger.info("Retrieving mentions")
    new_since_id = since_id
    for tweet in tweepy.Cursor(api.mentions_timeline,
        since_id=since_id).items():
        new_since_id = max(tweet.id, new_since_id)
        if tweet.in_reply_to_status_id is not None:
            continue
        
        og_tweet= api.get_status(tweet.in_reply_to_status_id_str)

        text= og_tweet.text; 
        author = og_tweet.name;

        createPic(text,author) # save a file called Quotes.jpg


        api.update_with_media( 
            filename= "Quotes.jpg",
            status="keep on quoting ... ",
            in_reply_to_status_id=tweet.id,
            )
    return new_since_id

def main():
    #api = create_api()
    since_id = 1
    while True:
        since_id = check_mentions(api, since_id)
        logger.info("Waiting...")
        time.sleep(60)

if __name__ == "__main__":
    main()