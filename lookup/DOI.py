import requests

DOI_BASE_URL = "http://dx.doi.org/"

class DOI:
    @staticmethod
    def doi_get(doi_number, kind="bibtex"):
        """
        Return a DOI entry in various formats given the DOI number. Formats may include

        * bibtex - returns a text string in bibtex format
        * json - returns a json object
        * turtle - returns a text string in xml turtle format

        Most convenient is the json format
        """

        if kind in ['bibtex']:
            headers = {"accept": "application/x-bibtex"}
        elif kind in ['json']:
            headers = {"accept": "application/json"}
        else:
            headers = {"accept": "text/turtle"}
        
        url = DOI_BASE_URL + doi_number

        r = requests.get(url, headers=headers)

        if kind in ["json"]:
            return r.json()
        else:
            return r.text
