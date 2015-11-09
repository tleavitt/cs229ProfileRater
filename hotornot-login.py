import urllib, urllib2, cookielib, time, argparse, requests


_USERNAME = "cool3can@gmail.com"
_PASSWORD = "tyqodiju"

# NOTE: THIS DOESN'T WORK.
# HotOrNot uses some SHA-1 Certificate trickery that makes logging in remotely difficult and annoying
# I don't think it's worth trying to figure out how to get around it; we should just scrape the data manually.
cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
opener.open("https://hotornot.com/")
login_data = urllib.urlencode({"email": _USERNAME, "password": _PASSWORD})
#resp = opener.open("https://hotornot.com/signin_popup/?ws=1&rt=d03162")
#resp = opener.open("https://hotornot.com/", login_data)

with open("sample-resp.html", "w") as outfile:
	out = resp.read()
	outfile.write(out)

