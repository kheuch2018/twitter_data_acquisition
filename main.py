from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import urllib
import re
import requests
import wget

headers = {
  "Authorization": "Bearer AAAAAAAAAAAAAAAAAAAAAJg4HAEAAAAAI7wVLWvggNhh7yVTgQZNUHb8BzU%3DmyJqu4rdLtFdHwwFxVgbyqBCMhGAZ2niVlWkLofq3ZFVDMMkEl"

}

r = requests.get("https://api.twitter.com/2/users/1186628409524404226/tweets?expansions=attachments.media_keys&media.fields=url", headers=headers)

twitter_data = r.json()["includes"]["media"]
links = []
for item in twitter_data:
  links.append(item['url'])

for i in range(len(links)-1):
    extension = links[i].split('.')[-1:][0]
    urllib.request.urlretrieve(links[i], "./images/file"+str(i)+"."+extension)




