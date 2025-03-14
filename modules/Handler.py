from modules.Scraper import Scraper
import json 
from pandas import pandas as pd

"""
[
    {
        "fund_description": "Family Unit TrustsFamily Charities  Ethical Trust (Accumulation Units)",
        "bid_price": "1100.00",
        "offer_price": "1100.00",
        "percent_change": "+ 0.46 %",
        "last_updated": "10 am 13/03/2025"
    }
]


"""


class Handler:

    def LoadData():
        with open('resp.json', 'r') as file:
            Stock = json.load(file)
            df = pd.DataFrame(Stock)

            StockData = {

                "bid_price" : df.loc[0, 'bid_price'],
                "offer_price": df.loc[0, 'offer_price'],
                "percent_change": df.loc[0, 'percent_change'],
                "last_updated": df.loc[0, 'last_updated']
            }


            



      


            

        


          

       



