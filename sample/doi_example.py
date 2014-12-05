from lookup.DOI import DOI
from lookup.IEEE import IEEE
from lookup.ORCID import ORCID
from lookup.CrossRef import CrossRef
from pprint import pprint
import json

# curl -D - -L -H "Accept: application/x-bibtex" "http://dx.doi.org/10.1109/GCE.2010.5676126"

# curl -D - -L -H "Accept:text/turtlex" http://dx.doi.org/10.1109/GCE.2010.5676126"


def banner(msg):
    print 70*"="
    print msg
    print 70*"="    


banner("doi turtle")
print DOI.doi_get("10.1109/GCE.2010.5676126", kind="turle")

banner("doi bibtex")
print DOI.doi_get("10.1109/GCE.2010.5676126")

banner("doi json")
pprint( DOI.doi_get("10.1109/GCE.2010.5676126", kind="json"))

banner("ieee xml")
print IEEE.ieee_doi_get("10.1109/GCE.2010.5676126", kind="xml")

banner("ieee json")
print IEEE.ieee_doi_get("10.1109/GCE.2010.5676126", kind="json")


banner("orcid xml")
print ORCID.orcid_doi_get("10.1109/GCE.2010.5676126", kind="xml")

banner("orcid json")
print json.dumps(ORCID.orcid_doi_get("10.1109/GCE.2010.5676126", kind="json"), indent=2)

banner("crossref json")
pprint( CrossRef.crossref_doi_get("10.1109/GCE.2010.5676126", kind="json"))