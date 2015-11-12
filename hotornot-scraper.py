from bs4 import BeautifulSoup
import urllib, urllib2, cookielib #, time, argparse, requests


_USERNAME = "cool3can@gmail.com"
_PASSWORD = "tyqodiju"


cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
login_data = urllib.urlencode({"email": _USERNAME, "password": _PASSWORD})
resp = opener.open("https://hotornot.com/", login_data)

print resp.read()

