import requests
import xmltodict
import json

IEEE_BASE_URL = "http://ieeexplore.ieee.org/gateway/ipsSearch.jsp?"

class IEEE:
    @staticmethod
    def ieee_author_search(author_name, kind="json"):
        """
        Return the author details from the author name. 

        * json - returns a json object
        * xml - returns a text string in xml turtle format

        Most convenient is the json format
        """
        
        url = IEEE_BASE_URL + "au=" + author_name
    
        r = requests.get(url)

        if kind in ["json"]:
            d = xmltodict.parse(r.text)      
            return json.dumps(d, indent=4)
        else:
            return r.text
    
    @staticmethod
    def ieee_doi_get(doi_number, kind="xml"):
        """
        Return a DOI entry from IEEE given the DOI number. 

        * json - returns a json object
        * xml - returns a text string in xml turtle format

        Most convenient is the json format
        """
        
        url = IEEE_BASE_URL + "doi=" + doi_number

        r = requests.get(url)

        if kind in ["json"]:
            d = xmltodict.parse(r.text)      
            return json.dumps(d, indent=4)
        else:
            return r.text
