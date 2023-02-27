import requests 
from config import Configuration

def search_names(term):
    url = requests.get('https://partners.every.org/v0.2/search/{}'.format(term), 
                       params={"apiKey": Configuration.SECRET_KEY, "take": 3})
    
    return url.json()
