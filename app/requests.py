import requests,json
from .models import Quote

url = "http://quotes.stormconsultancy.co.uk/random.json"

def get_quotes():
    response = requests.get(url).json()
    random_quote = Quote(response.get("author"), response.get("quote"))
    return random_quote
