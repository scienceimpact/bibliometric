import requests

ORCID_BASE = "http://pub.orcid.org/"

def author_details(name, kind="json"):
    """
    Return the author details from ORCID. 

    * json - returns a json object
    * xml - returns a text string in xml turtle format

    Most convenient is the json format
    """
        
    url = ORCID_BASE + name


    if kind in ["xml"]:
        r = requests.get(url)
        return r.text
    if kind in ["json"]:
        headers = {"accept": "application/name+json"}        
        r = requests.get(url, headers=headers)
        return r.json()