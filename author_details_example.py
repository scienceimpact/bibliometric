from scienceimpact.lookup.orcid_author_details import author_details
from pprint import pprint
import json


def banner(msg):
    print 70*"="
    print msg
    print 70*"=" 
    
banner("orcid author details xml")
print author_details("0000-0001-9558-179X", kind="xml")

banner("orcid author details json")
print json.dumps(author_details("0000-0001-9558-179X", kind="json"), indent=2)
