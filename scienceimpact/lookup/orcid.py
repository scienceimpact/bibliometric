import requests
import xmltodict
import json

# Other examples:
# http://support.orcid.org/knowledgebase/articles/132354-searching-with-the-public-api

DOI_BASE = "http://pub.orcid.org/v1.1/search/orcid-bio/?q=digital-object-ids:%"

# curl -H "Accept: application/orcid+json" "10.1109/GCE.2010.5676126"

def doi(doi_number, kind="json"):
    """
    Return a doi entrty from IEEE. 

    * json - returns a json object
    * xml - returns a text string in xml turtle format

    Most convenient is the json format
    """
        
    url = DOI_BASE + doi_number


    if kind in ["xml"]:
        # headers = {"accept": "application/orcid+json"}
        r = requests.get(url)
        return r.text
    if kind in ["json"]:
        headers = {"accept": "application/orcid+json"}        
        r = requests.get(url, headers=headers)
        return r.json()




    
