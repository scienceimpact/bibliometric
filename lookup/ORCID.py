import requests

ORCID_BASE_URL = "http://pub.orcid.org/"

class ORCID:
    @staticmethod
    def orcid_author_search(author_name, kind="json"):
        """
        Return the author details from the author name. 

        * json - returns a json object
        * xml - returns a text string in xml turtle format

        Most convenient is the json format
        """
        
        url = ORCID_BASE_URL + "search/orcid-bio?q=" + author_name

        if kind in ["xml"]:
            r = requests.get(url)
            return r.text
        if kind in ["json"]:
            headers = {"accept": "application/name+json"}        
            r = requests.get(url, headers=headers)
            return r.json()
    
    @staticmethod
    def orcid_author_get(orcid, kind="json"):
        """
        Return the author details from the ORCID. 

        * json - returns a json object
        * xml - returns a text string in xml turtle format

        Most convenient is the json format
        """
        
        url = ORCID_BASE_URL + orcid

        if kind in ["xml"]:
            r = requests.get(url)
            return r.text
        if kind in ["json"]:
            headers = {"accept": "application/orcid+json"}        
            r = requests.get(url, headers=headers)
            return r.json()

    @staticmethod
    def orcid_doi_get(doi_number, kind="json"):
        """
        Return a DOI entry from OrcID given the DOI number. 

        * json - returns a json object
        * xml - returns a text string in xml turtle format

        Most convenient is the json format
        """
        
        url = ORCID_BASE_URL + "v1.1/search/orcid-bio/?q=digital-object-ids:%" + doi_number

        if kind in ["xml"]:
            r = requests.get(url)
            return r.text
        if kind in ["json"]:
            headers = {"accept": "application/orcid+json"}        
            r = requests.get(url, headers=headers)
            return r.json()
    
    @staticmethod
    def orcid_author_works_get(orcid, kind="json"):
        """
        Return the author works from the ORCID. 

        * json - returns a json object
        * xml - returns a text string in xml turtle format

        Most convenient is the json format
        """
        
        url = ORCID_BASE_URL + orcid + "/orcid-works"

        if kind in ["xml"]:
            r = requests.get(url)
            return r.text
        if kind in ["json"]:
            headers = {"accept": "application/orcid+json"}        
            r = requests.get(url, headers=headers)
            return r.json()
