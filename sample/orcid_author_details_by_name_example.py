from scienceimpact.lookup.orcid_search_author_details_by_orcid import author_details
from scienceimpact.lookup.orcid_author_works import author_works
import json

fout = open("orcid_author_details.txt", "w")

def banner(msg):
    print >>fout,70*"="
    print >>fout,msg
    print >>fout,70*"=" 
    
banner("orcid author details xml")
print >>fout,author_details("0000-0001-9558-179X", kind="xml").encode('utf-8')

banner("orcid author details json")
print >>fout,json.dumps(author_details("0000-0001-9558-179X", kind="json"), indent=2).encode('utf-8')

banner("orcid author works xml")
print >>fout,author_works("0000-0001-9558-179X", kind="xml").encode('utf-8')

banner("orcid author works json")
print >>fout,json.dumps(author_works("0000-0001-9558-179X", kind="json"), indent=2).encode('utf-8')
