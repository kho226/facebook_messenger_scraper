'''
A module to send a random sms from a MongoDB
'''

from pymongo import MongoClient
from twilio.rest import Client
import pprint
from random import randint
import os
import sys

#create MongoClient
client = MongoClient('localhost', 27017)

#databases and collections are created lazily in MongDB
db = client['moti-db']
collection = db['messages']

random = randint(1487943362906,1500000000000)
print (random)

payload = collection.find_one({"time_stamp":str(random)})
print payload


try:
    account_sid = sys.argv[1]
    auth_token = sys.argv[2]
    receiver = sys.argv[3]
    sender = sys.argv[4]
except IndexError:
    print ("Usage: python send_random_sms.py <twilio_account_sid> <twilio_auth_token> <receiver_phone#> <sender_phone#>")

def send_random_sms(account_sid, auth_token, receiver, sender):
    #twilio verification
    client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)


    print ("Now sending...")
    #pprint.pprint(collection.find_one({time_stamp:randint(0,15000000000000)}).content)
    pprint.pprint(payload)
    print ("to " + receiver)

    client.messages.create(
        to=receiver,
        from_=sender,
        body=payload,
        media_url="",
    )

send_random_sms()
