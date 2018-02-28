import httplib2
import json


def grab():
    url = ('https://api.coinmarketcap.com/v1/ticker/?limit=10')
    h = httplib2.Http()
    response, content = h.request(url, 'GET ')
    result = json.loads(content )
    return result


a = grab()
