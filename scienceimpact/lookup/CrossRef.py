import requests

CROSSREF_BASE_URL = "http://search.crossref.org/dois?q="

class CrossRef:
    @staticmethod
    def crossref_author_search(author_name, kind="json"):
        """
        Return the author details from the author name. 

        * json - returns a json object

        Most convenient is the json format
        """

        if kind in ['json']:
            headers = {"accept": "application/json"}
          
        url = CROSSREF_BASE_URL + author_name

        r = requests.get(url, headers=headers)

        if kind in ["json"]:
            return r.json()

    @staticmethod
    def crossref_doi_get(doi_number, kind="json"):
        """
        Return a DOI entry from CrossRef given the DOI number.

        * json - returns a json object

        Most convenient is the json format
        """

        if kind in ['json']:
            headers = {"accept": "application/json"}
          
        url = CROSSREF_BASE_URL + doi_number

        r = requests.get(url, headers=headers)

        if kind in ["json"]:
            return r.json()
