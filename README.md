# DS3001-ProjectTwo
Project two for DS 3001 


## How to Run Locally
1. git clone 
2. docker build --tag quote-bot .
3. docker run -i quote-bot

## Export as Tar File for AWS
*Do this outside the repo*
1. docker save quote-bot:latest | gzip > quote-bot.tar.gz