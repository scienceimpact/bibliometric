import requests
import xmltodict
import json

IEEE_BASE = "http://ieeexplore.ieee.org/gateway/ipsSearch.jsp?au="

def author_details(author_name, kind="json"):
    """
    Return the author details from Author name. 

    * json - returns a json object
    * xml - returns a text string in xml turtle format

    Most convenient is the json format
    """
        
    url = IEEE_BASE + author_name
    
    r = requests.get(url)

    if kind in ["json"]:
        d = xmltodict.parse(r.text)      
        return json.dumps(d, indent=4)
    else:
        return r.text