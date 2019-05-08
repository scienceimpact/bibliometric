from lookup.ORCID import ORCID
import json

fout = open("orcid_author_details_by_name.txt", "w")

def banner(msg):
    print(70 * "=", file=fout)
    print(msg, file=fout)
    print(70 * "=", file=fout) 
    
banner("orcid author details xml")
print(ORCID.orcid_author_search("gregor von laszewski", kind="xml").encode('utf-8'), file=fout)

banner("orcid author details json")
print(json.dumps(ORCID.orcid_author_search("gregor von laszewski", kind="json"), indent=2).encode('utf-8'), file=fout)
