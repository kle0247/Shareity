import requests 
from config import Configuration

def search_names(term):
    try:
        url = requests.get('https://partners.every.org/v0.2/search/{}'.format(term), 
                        params={"apiKey": Configuration.SECRET_KEY, "take": 9})
    except:
        return "There was an issue grabbing data"
    return url.json()
