import requests
from bs4 import BeautifulSoup
import json

stock_data = 'resp.json'
class Scraper:

     def Scrape():
        url = "https://www.onefamily.com/help/fund-information/daily-prices/"
        USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X x.y; rv:42.0) Gecko/20100101"
        headers = {"user-agent": USER_AGENT}
        
        resp = requests.get(url, headers=headers)
        content = BeautifulSoup(resp.content, 'html.parser')

        table = content.find('table', class_='tabbeddaily_prices')
        stock_data_list = []

        if table:
            rows = table.find_all('tr')

            for row in rows[1:]:  
                columns = row.find_all('td')
                if len(columns) >= 5:
                    fund_description = columns[0].get_text(strip=True)
                    bid_price = columns[1].get_text(strip=True)
                    offer_price = columns[2].get_text(strip=True)
                    percent_change = columns[3].get_text(strip=True)
                    last_updated = columns[4].get_text(strip=True)
                    
                    stock_data_list.append({
                        "fund_description": fund_description,
                        "bid_price": bid_price,
                        "offer_price": offer_price,
                        "percent_change": percent_change,
                        "last_updated": last_updated
                    })
        return stock_data_list
     
     
     

     

     def StoreData():
                data = Scraper.Scrape()
                if data:
                    with open(stock_data, 'w') as json_file:
                        json.dump(data, json_file, indent=4)
                    print("saved")
                else:
                     print("no data")

