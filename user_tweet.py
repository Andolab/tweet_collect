import json
import config
from requests_oauthlib import OAuth1Session

CK = config.CONSUMER_API_KEY
CS = config.CONSUMER_API_SELECT_KEY
AT = config.ACCESS_TOKEN
ATS = config.ACCESS_TOKEN_SECRET
oauth = OAuth1Session(CK, CS, AT, ATS)
endpoint = "https://api.twitter.com/1.1/statuses/user_timeline.json"

params = {"screen_name":"****","exclude_replies":True, "count":200}
json_list = []
for i in range(16):
  response = oauth.get(endpoint, params=params)

  if response.status_code == 200:
    tweets = json.loads(response.text)
    params["max_id"] = tweets[-1]['id']
    json_list += [line for line in tweets]
  else:
    print("Failed :%d" % response.status_code)

with open("test.json", "a") as f:
  json.dump(json_list, f)
