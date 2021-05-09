# DS3001-ProjectTwo
Project Two for DS 3002 


## Project Description
For this project, we were given the opportunity to write an interactive, Twitter based bot account that can recieve and parse Tweets and return a data-driven reply. As explained in the video, the main motivation and inspiration for this project came from the fact that there are a lot of interesting quotes on Twitter but not an easy (and fun) way to save them.

## Example of Twitter Bot's Replies

<p align = "center">
  <img width="401" alt="Screen Shot 2021-05-09 at 7 11 31 PM" src="https://user-images.githubusercontent.com/60242580/117589882-6eabd680-b0fa-11eb-951b-560dfccf0611.png">
</p>

Here, we can see two examples of the bot at work. We can see that with each response, there is a randomly selected text that goes with the reply. For example, in the first response, the bot decided to say "to quote or not to quote" and on the second "quote bot likes your quotes, keep quoting". Below is a closer-up version of each of the quotes. Ms. Quote Bot does a great job of nicely formatting each of the original Tweets and returning it to the user who replied to it.

Example One:

<p align="center">
  <img width="296" alt="Screen Shot 2021-05-09 at 7 12 49 PM" src="https://user-images.githubusercontent.com/60242580/117589905-9dc24800-b0fa-11eb-8589-3fb77c0c113b.png">
</p>


Example Two: 

<p align="center">
  <img width="313" alt="Screen Shot 2021-05-09 at 7 13 42 PM" src="https://user-images.githubusercontent.com/60242580/117589917-bc284380-b0fa-11eb-8212-d6aef5fb97eb.png">
</p>


As we can see above, there are many templates that Ms. Quote Bot can choose to put the quote on.  

## Video with Code Walkthrough and Live Demonstration 
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

Thank you for viewing our project! It was extremely fun to work on, and we hope you enjoyed learning more about it.
