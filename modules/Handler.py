from modules.Scraper import Scraper
import json 
from pandas import pandas as pd

class Handler:

    def LoadData():

        #load data 
        with open('resp.json', 'r') as file:
            Stock = json.load(file)
            df = pd.DataFrame(Stock)

            #create dict for acessing values 
            StockData = {
                "bid_price" : df.loc[0, 'bid_price'],
                "offer_price": df.loc[0, 'offer_price'],
                "percent_change": df.loc[0, 'percent_change'],
                "last_updated": df.loc[0, 'last_updated']
            }
            return StockData


            



      


            

        


          

       



