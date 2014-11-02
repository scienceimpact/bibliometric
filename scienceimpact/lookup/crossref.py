import requests

DOI_BASE = "http://search.crossref.org/dois?q="

def doi(doi_number, kind="json"):
  """
  Return a doi entry from CrossRef

  * json - returns a json object

  Most convenient is the json format
  """

  if kind in ['json']:
    headers = {"accept": "application/json"}
          
  url = DOI_BASE + doi_number

  r = requests.get(url, headers=headers)

  if kind in ["json"]:
      return r.json()
