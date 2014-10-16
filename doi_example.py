from scienceimpact.lookup.doi import doi as doi_crossref
from scienceimpact.lookup.ieee import doi as doi_ieee
from pprint import pprint
import json


def banner(msg):
    print 70*"="
    print msg
    print 70*"="    

"""
banner("crossref turtle")
print doi_crossref("10.1109/GCE.2010.5676126", kind="turle")

banner("crossref bibtex")
print doi_crossref("10.1109/GCE.2010.5676126")

banner("crossref json")
pprint( doi_crossref("10.1109/GCE.2010.5676126", kind="json"))
"""
    
banner("ieee xml")
print doi_ieee("10.1109/GCE.2010.5676126", kind="xml")

banner("ieee xml")
print doi_ieee("10.1109/GCE.2010.5676126", kind="json")


# curl -D - -L -H "Accept: application/x-bibtex" "http://dx.doi.org/10.1109/GCE.2010.5676126"

# curl -D - -L -H "Accept:text/turtlex" http://dx.doi.org/10.1109/GCE.2010.5676126"
