from modules.Scraper import Scraper
from modules.Handler import Handler

#scraper object 
data = Scraper
data.Scrape()
data.StoreData()


# json handle 

handle = Handler
handle.LoadData()
