### Project setup

```
pip install virtualenv
git clone https://github.com/kho226/facebook_messenger_scraper
cd facebook_messenger_scraper
virtualenv -p usr/bin/python2.6
source bin/activate
pip install urllib2
pip install requests
pip install twilio
pip install splinter
pip install pymongo
mongod
```

### MongoDB setup
https://ademirgabardo.wordpress.com/2016/02/02/installing-and-running-mongodb-on-mac-osx-for-beginners/

### splinter
http://splinter.readthedocs.io/en/latest/index.html

### twilio
https://github.com/twilio/twilio-python

https://www.twilio.com/docs/api/rest/sending-messages


### MongoDB
https://docs.mongodb.com/manual/

### get_friends.py

Get all of your friend's Facebook user ids from your messaging history.

```
Usage: python get_friends.py username password output_file
```

The output has the following format: id \t name \t username

### collect_conversations.py
Downloads your entire Facebook messaging history.

```
Usage: python collect_conversations.py username password your_facebook_id friend_file output_dir
```
You can find your Facebook ID by digging in the HTML. This script will store each conversation in a .txt file named after your friend's username, in the provided output directory. This script also takes as input a tab-delimited file containing your friends' user ids, names, and usernames. You can manually compile this or generate it using the get_friends.py script.

This script will then store each individual message into a MongoDB named 'messages'. Each entry into the database is structured as follows
```
message_collection = {
  "content" : " ",
  "time_stamp " : " " ,
  "device_type" :  " ",
  "sender" " "
}
```

### send_random_sms.py

```
Usage: python send_random_sms.py twilio_account_sid twilio_auth_token receiver_phone# sender_phone#
