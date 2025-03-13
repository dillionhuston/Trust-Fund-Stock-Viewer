import requests
from bs4 import BeautifulSoup

url = "https://www.onefamily.com/help/fund-information/daily-prices/" 
USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X x.y; rv:42.0) Gecko/20100101"
headers = {"user-agent": USER_AGENT}
resp = requests.get(url, headers=headers)
BeautifulSoup(resp.content, "html.parser" )
print(resp.text)
