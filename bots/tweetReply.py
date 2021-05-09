#!/usr/bin/env python
# tweepy-bots/bots/autoreply.py

import tweepy
import logging
#from config import create_api
import time
import os

import random

quote_list = [ "quote created...", "thanks for your quote!", "keep on quoting!", "quote bot likes your quote, keep sharing", "a quote a day keeps the bot away...", "share a quote, save a life", "you will die but your quotes will live forever", "share memories, make quotes..." , "oh hey, a quote!", "quote-tastic!", "Linkedin would be proud", "wow, you're a quote master", "to quote or not to quote", "don't be basic, keep on quoting", "this will live in history books", "make an impression, make a quote", "an icon in making"]

# foo = ['a', 'b', 'c', 'd', 'e']
# print(random.choice(foo))
# print("-------")
# twitter_keys = {
#         'consumer_key':        'YxD13yQdWjKla3FAn2PgLFnkS',
#         'consumer_secret':     '3nw1BrnXTIeUBcgFKRAIKrqypT9t39qq0di2tZYE1gwHpeuXKD',
#         'access_token_key':    '1391110880297984005-aealTh3bgjh2N7oeXXQhJDcjHPLLxQ',
#         'access_token_secret': '3eO1P1dRwLDio4ZfSUXUOx8FgLKagUEQaZeUqf5Tn8YZs'
#     }

twitter_keys = {
        'consumer_key':        'HKga97Bq5SGKyCmb7lrA4RbMf',
        'consumer_secret':     'qU3hudMNlORo3t9lBLBEOlbnVKgtcvmdLpHOHiqZwauP3OguPI',
        'access_token_key':    '1391110880297984005-DtOjCFvJUjpsHNoLpOh2Zr73CnA8O2',
        'access_token_secret': 'kZrfzy4FjYGg3rxqTyp1D5JwGdQjZPHYTevb7hwgostcP'
    }


#Setup access to API
auth = tweepy.OAuthHandler(twitter_keys['consumer_key'], twitter_keys['consumer_secret'])
auth.set_access_token(twitter_keys['access_token_key'], twitter_keys['access_token_secret'])

api = tweepy.API(auth)



logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


def createPic(text, author):
    # os.system("python3 quotesmaker.py -q \" " + text + " \" -a \" " + author +" \"   " )      

    os.system("cd bots; python3 quotesmaker.py -q \" " + text + " \" -a \" " + author +" \"   ;cd .." )
    
    logger.info("Created pic that says: \n  " + text + " by " + author +  "\n\n" )

def check_mentions(api, since_id):
    logger.info("Retrieving mentions")
    new_since_id = since_id
    for tweet in tweepy.Cursor(api.mentions_timeline, since_id=since_id).items():
        print(tweet.text,tweet.id,since_id)
        new_since_id = max(tweet.id, new_since_id)
        
        # if tweet.in_reply_to_status_id is not None:
        #     continue
        
        
        og_tweet= api.get_status(tweet.in_reply_to_status_id_str)

        text= og_tweet.text; 
        author = tweet.in_reply_to_screen_name;

        
        createPic(text,author) # save a file called Quotes.jpg

        try:
            api.update_with_media( 
                filename= "bots/Quotes.jpg",
                status= "@" + tweet.user.screen_name + " " + random.choice(quote_list),
                in_reply_to_status_id=tweet.id,
                )

        except:
            logger.warning("failed to reply")

        logger.info("Made Image for " + tweet.user.screen_name ) 
       
        
        dmText1= """ Hey! Thanks for trying out this tool created by @ChristianFJung and @Jasmine_Dogu."""
        dmText2 = """  We'd appreciate any help you can give us to support this project. Just mention Ms. Quote Bot :) paypal.me/christianfjung"""

        try:
            api.send_direct_message(tweet.user.id, dmText1)
            api.send_direct_message(tweet.user.id, dmText2)
            logger.info("sent DMs"  ) 
        except:
            logger.warning("failed to reply")

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