# DS3001-ProjectTwo
Project two for DS 3001 


https://user-images.githubusercontent.com/60242580/117589715-3ce64000-b0f9-11eb-9316-d4d494337349.mp4


## How to Run Locally
1. git clone 
2. docker build --tag quote-bot .
3. docker run -i quote-bot

## Export as Tar File for AWS
*Do this outside the repo*
1. docker save quote-bot:latest | gzip > quote-bot.tar.gz

You can then upload this file to AWS. *(See the real python article for more information)* 


## Sources Cited
1. Real Python How to Make a Twitter Bot- https://realpython.com/twitter-bot-python-tweepy/

2. Quotes-maker library https://github.com/adityagirinv/quotes-maker

3. Tweepy Documentation
