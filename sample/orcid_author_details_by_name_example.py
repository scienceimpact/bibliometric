from lookup.ORCID import ORCID
import json

fout = open("orcid_author_details.txt", "w")

def banner(msg):
    print >>fout,70*"="
    print >>fout,msg
    print >>fout,70*"=" 
    
banner("orcid author details xml")
print >>fout,ORCID.orcid_author_get("0000-0001-9558-179X", kind="xml").encode('utf-8')

banner("orcid author details json")
print >>fout,json.dumps(ORCID.orcid_author_get("0000-0001-9558-179X", kind="json"), indent=2).encode('utf-8')

banner("orcid author works xml")
print >>fout,ORCID.orcid_author_works_get("0000-0001-9558-179X", kind="xml").encode('utf-8')

banner("orcid author works json")
print >>fout,json.dumps(ORCID.orcid_author_works_get("0000-0001-9558-179X", kind="json"), indent=2).encode('utf-8')
