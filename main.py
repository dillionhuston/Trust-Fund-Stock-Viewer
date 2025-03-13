import requests
from bs4 import BeautifulSoup
import html_to_json

stock_data = 'resp.json'


def Scrape():
    url = "https://www.onefamily.com/help/fund-information/daily-prices/" 
    USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X x.y; rv:42.0) Gecko/20100101"
    headers = {"user-agent": USER_AGENT}
    resp = requests.get(url, headers=headers)
   
    if resp.status_code == 200:
        page_soup = BeautifulSoup(resp.content, "html.parser")
        return page_soup 
    else:
        print(f"failed status code: {resp.status_code}")
        return None  


def StoreData():
    page_soup = Scrape()  
    
    if page_soup:
      
        data_output = html_to_json.convert(str(page_soup))  
        print(data_output)
      
        with open(stock_data, 'w') as json_file:
            json_file.write(str(data_output)) 
        print("ni data.")

Scrape()  
StoreData()  
