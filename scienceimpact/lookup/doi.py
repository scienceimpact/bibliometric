import requests

DOI_BASE = "http://dx.doi.org/"

def doi2bibtex(doi, kind="bibtex"):
  """
  Return a bibTeX entry as a string for a given DOI.
  """

  if kind in ['bibtex']:
    headers = {"accept": "application/x-bibtex"}
  elif kind in ['json']:
    headers = {"accept": "application/json"}
  else:
    headers = {"accept": "text/turtle"}    
        
  url = DOI_BASE + doi

  r = requests.get(url, headers=headers)

  if kind in ["json"]:
      return r.json()
  else:
      return r.text
