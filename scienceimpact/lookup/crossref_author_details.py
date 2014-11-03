import requests

CROSSREF_BASE = "http://search.crossref.org/dois?q="

def author_details(author_name, kind="json"):
    """
    Return the author details from Author name. 

    * json - returns a json object

    Most convenient is the json format
    """

    if kind in ['json']:
        headers = {"accept": "application/json"}
          
    url = CROSSREF_BASE + author_name

    r = requests.get(url, headers=headers)

    if kind in ["json"]:
        return r.json()
