'''
Get all of your friend's facebook user ids from your messaging history.
Usage: python get_friends.py <username> <password> <output file>

The output has the following format: id \t name \t username

Uses a browser automation library and the Phantom JS browser.
brew install phantomjs
pip install splinter
'''

import sys
import json
import time
import selenium
import requests
from splinter import Browser
from urllib2 import URLError

_base_url = "https://www.facebook.com/messages"
_login_url = "https://login.facebook.com/login.php?login_attempt=1"
_base_msg_url = _base_url + "/messages/"

try:
	username = sys.argv[1]
	password = sys.argv[2]
	out = sys.argv[3]
	print (username)
	print (password)
	print (out)
except IndexError:
	print "Usage: python get_friends.py <username> <password> <output file>"
	sys.exit()

# Create the phantom js browser instance
# browser = selenium.webdriver.PhantomJS()
# browser.set_window_size(1920,1080)
browser = Browser('firefox')

# Log in by finding the log in form and filling it
# with your username and password. Then automatically
# "click" on the enter button, and navigate to the
# messages page.
def login():
	browser.visit(_base_url)
	#inputs = browser.find_by_id("login_form")[0].find_by_tag("input")
	#inputs[1].fill(username)
	#inputs[2].fill(password)
	##browser.set_window_size(1920, 1080)

	browser.fill('email',username)
	browser.fill('pass',password)

	enter = browser.find_by_id('loginbutton')
	enter.click()
	#browser.find_by_css("input[name='Log In']").click()
	print "Logged in!"
	var = raw_input("hit 'enter' once the page has finished loading...")
	#browser.visit(_base_msg_url)
	#print ("we at the messenger!")



# This is the automatic equivalent of scrolling up.
def load_more():
	# Messages are contained within these divs
	showOlderbtn = browser.find_by_tag('a')
	for x in showOlderbtn:
		if x.value == "Show Older":
			x.click()
			print("loading more conversations...")
			return True



# Once all threads have been loaded, call this function to
# get all the user ids and save them to a file.
def get_threads():
	#print ("get_threads")
	f = open(out, 'w')
	# Each thread is stored in a list element with class _k-

	divs = browser.find_by_tag('div')
	globalContainer = divs.find_by_id("globalContainer")
	content = globalContainer.find_by_id('content')
	test = browser.find_by_tag("span")
	divs = test.find_by_tag('div')
	count = 0
	#for x in test:
		#print x
		#count += 1
	#print (count)


	#print (id1)
	#print (id2)

	a = browser.find_by_tag('a')

	ul = browser.find_by_tag('ul')
	conversationList = ul[1]
	#get all conversations
	li = conversationList.find_by_tag('li')
	for x in li:
		name = x.find_by_tag('span')
		timestamp = x.find_by_tag('abbr')
		username = x.find_by_tag('a')['data-href'].split('/')[-1]
		userid = x.find_by_tag('div')['id'].split(':')[-1]
		print (name.value)
		print (username)
		print (userid)
		f.write(userid + '\t' + name.value + '\t'+ username.encode("utf8") + '\n')
	f.close()

# Log in to Facebook
login()

# Keep loading new threads

while True:
	try:
		loaded_more = load_more()
		if not loaded_more:
			break
		time.sleep(1)
	except (URLError, selenium.common.exceptions.StaleElementReferenceException):
		print "reconnecting......"
		# Try to reconnect
		time.sleep(5)
		try:
			login()
		except:
			continue

# Now that all threads have been loaded in the HTML,
# get all your friends' information
get_threads()
