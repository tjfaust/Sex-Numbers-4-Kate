from twython import Twython
import csv
import datetime
import secrets

day1 = datetime.datetime(2014, 4, 24)
tooday = datetime.datetime.now()
gap = tooday - day1
gap = gap.days
gap = gap + 1
tooday = tooday.strftime("%m/%d")

#print ("Day 1 is " + day1.strftime("%m/%d"))
#print("Today is " + tooday.strftime("%m/%d"))
#print (gap.days)

APP_KEY = secrets.APP_KEY  # Customer Key here
APP_SECRET = secrets.APP_SECRET  # Customer secret here
OAUTH_TOKEN = secrets.OAUTH_TOKEN  # Access Token here
OAUTH_TOKEN_SECRET = secrets.OAUTH_TOKEN_SECRET  # Access Token Secret here

twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

with open ('kdates.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    data = [row for row in reader]
    todayCountry =(data[gap][1])
    sexnum = (data[gap][3])

newTweet = "Hi Kate! Today (in Houston), you are in " + todayCountry + ". It is %s and the sex number there is " % (tooday) + sexnum
newTweet = newTweet[:139]
#print (newTweet)

#print("You are in country %d" % (country))
twitter.update_status(status=newTweet)
