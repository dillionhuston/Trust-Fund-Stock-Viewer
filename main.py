from modules.Scraper import Scraper
from modules.Handler import Handler
from modules.WebView import WebView
#scraper object 
data = Scraper
data.Scrape()
data.StoreData()


# json handle 
handle = Handler
handle.LoadData()

# enable webview
web = WebView()
web.get_data() # type: ignore
