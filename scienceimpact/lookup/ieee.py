import requests
import xmltodict
import json

DOI_BASE = "http://ieeexplore.ieee.org/gateway/ipsSearch.jsp?doi="

#curl -D - -L "http://ieeexplore.ieee.org/gateway/ipsSearch.jsp?doi=10.1109/GCE.2010.5676126"

def doi(doi_number, kind="xml"):
  """
  Return a doi entrty from IEEE. 

  * json - returns a json object
  * xml - returns a text string in xml turtle format

  Most convenient is the json format
  """
        
  url = DOI_BASE + doi_number

  r = requests.get(url)


  if kind in ["json"]:
      d = xmltodict.parse(r.text)      
      return json.dumps(d, indent=4)
  else:
      return r.text




    
