'''
import tweepy
import os
import json
import sys
import geocoder
# API Keys and Tokens
consumer_key = os.environ['API_KEY']
consumer_secret = os.environ['API_SECRET_KEY']
access_token = os.environ['ACCESS_TOKEN']
access_token_secret = os.environ['ACCESS_TOKEN_SECRET']

# Authorization and Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

if __name__ == "__main__":
    # Available Locations
    available_loc = api.available_trends()
    # writing a JSON file that has the available trends around the world
    with open("available_locs_for_trend.json","w") as wp:
        wp.write(json.dumps(available_loc, indent=1))

    # Trends for Specific Country
    loc = sys.argv[1]     # location as argument variable 
    g = geocoder.osm(loc) # getting object that has location's latitude and longitude

    closest_loc = api.closest_trends(g.lat, g.lng)
    trends = api.get_place_trends(closest_loc[0]['woeid'])
    # writing a JSON file that has the latest trends for that location
    with open("twitter_{}_trend.json".format(loc),"w") as wp:
        wp.write(json.dumps(trends, indent=1))
        
'''
import twint

#configuration
c=twint.Config()
c.Hide_output=False #but it ignores this
c.Store_object=True
c.Store_csv=True
c.Since="2020-09-01"
c.User_full=True
c.Limit=100 #I have tested up to 1000 ok
c.Output="testing.csv" #but it ignores this

srchname="(from:RealDonaldTrump)"
srch=srchname+" max_id:"+str(1307047063197224961)

twint.run.Search(c)
tlist = c.search_tweet_list
print(tlist)