from modules.Scraper import Scraper
import json 
from pandas import pandas as pd

class Handler:

    
    

    def LoadData():
        with open('resp.json') as file:
            Stock = json.load(file)
            print(Stock)