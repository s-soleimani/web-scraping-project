# -*- coding: utf-8 -*-
"""my.ipynb
***myEmail : roz.sorkh@gmail.com***
"""

import requests
import re
import urllib

def get_next_target(content):
  start_link = content.find('<a href=')
  if start_link == -1:
      return None,0
  start_quote = content.find('"',start_link)
  end_quote = content.find('"', start_quote+1)
  url = content[start_quote+1 : end_quote]
  return url , end_quote

def Save_IntoFile_all_links(page_content):
  while True:
    url,end_quote = get_next_target(page_content)
    if url:      
      with open('UrlFile.csv', 'a') as f:
        f.write(url)
        f.write("\n")
      page_content = page_content[end_quote:]
    else:
      break

def getAddress(PageAddress):
  page_url = PageAddress
  page_content = urllib.request.urlopen(page_url).read()
  page_content = page_content.decode()
  page_content
  Save_IntoFile_all_links(page_content)

getAddress("https://www.bbc.com/news/world-europe-60096261")

getAddress("https://www.bbc.com/news/world-europe-60090991")

getAddress("https://www.bbc.com/sport/live/football/59185815")

getAddress("https://www.bbc.co.uk/news/entertainment-arts-60082456")

getAddress("https://www.bbc.co.uk/news/entertainment-arts-60082456")

