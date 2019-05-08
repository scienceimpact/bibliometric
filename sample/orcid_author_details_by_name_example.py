from lookup.ORCID import ORCID
import json

fout = open("orcid_author_details.txt", "w")

def banner(msg):
    print(70 * "=", file=fout)
    print(msg, file=fout)
    print(70 * "=", file=fout) 
    
banner("orcid author details xml")
print(ORCID.orcid_author_get("0000-0001-9558-179X", kind="xml").encode('utf-8'), file=fout)

banner("orcid author details json")
print(json.dumps(ORCID.orcid_author_get("0000-0001-9558-179X", kind="json"), indent=2).encode('utf-8'), file=fout)

banner("orcid author works xml")
print(ORCID.orcid_author_works_get("0000-0001-9558-179X", kind="xml").encode('utf-8'), file=fout)

banner("orcid author works json")
print(json.dumps(ORCID.orcid_author_works_get("0000-0001-9558-179X", kind="json"), indent=2).encode('utf-8'), file=fout)
