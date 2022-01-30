# helloSpace2021
- Twitter bot created for JSC hackathon 2022

**Features**:
1) Reply to mentions and corresponding hashtag - tweets with #activitiesjsc2022 will be automatically replied with a DIY activity from the Nasa JSC website (https://spacecenter.org/community-science/)

2) Tweet out 3 space facts a day - created csv with the facts and bot will tweet out 3 in a specified interval

**Requirements**
- .env / config file was used to set up consumer keys and tokens. These were acquired from the Twitter developer website and sign-up

**Resources**
- Python was used to code the entire project, utilizing Tweepy to access the Twitter API (v2) and pandas to manipulate csv data
- The app was deployed in Heroku successfully with the bot.py file being the designated worker. The app has since been on offline mode in Heroku to prevent rate limits from exceeding. 
