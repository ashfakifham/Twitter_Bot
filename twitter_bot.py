import tweepy as tp
import keys as key
import json

# setting authentication for the api
auth = tp.OAuthHandler(key.consumer_key, key.consumer_secret)
auth.set_access_token(key.access_token, key.access_token_secret)

# creating api object
api = tp.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
my_id = "" # for user ID

# to get user entry for days count and tweet to be posted
# day = input("Enter which day this is")
# time_spent = input("Enter how long you coded")
day_counter = []
day_count=1




statuses =api.user_timeline(my_id, count = 2) #extracting the last  2 status updates
tweet = statuses[0]
data = json.dumps(tweet._json, indent = 2) #creates a json object ( json string)
data_2 = json.loads(data) # converts a json string to python objects based on json convertion logic

#for status in statuses:
   #print(status.text)
   # my_day, my_num, my_data = str(status.text).split(" ",2) # only splits to a max of 2 spaces
   # day_counter.append(int(my_num))

#day_count += max(day_counter)
status = "Day {} of my #100DaysOfCode Challenge:\nCompleted the twitter bot development and this is its first tweet!".format(day_count)
print(data_2['text'])

# api.update_status(status)
#api.update_status("Im a bot and lets hope I work!")
# user = api.get_user(sreen_name = "") to get a specific user's ID to dm
# print(user.id) # extracting the id value form the json file
# api.send_direct_message(user.id,"Since im working, Happy tweeting!") #DM