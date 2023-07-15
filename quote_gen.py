import requests

def get_quotes():
    req=requests.get("https://zenquotes.io/api/random")
    data=req.json()
    quote=data[0]['q']+" - "+data[0]['a']
    return quote
