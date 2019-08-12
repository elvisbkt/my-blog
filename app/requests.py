import urllib.request,json
from .models import Quote



def get_quote():

    with urllib.request.urlopen('http://quotes.stormconsultancy.co.uk/random.json') as url:
        quote_details_data = url.read()
        quote_details_response = json.loads(quote_details_data)

        

    return quote_object

