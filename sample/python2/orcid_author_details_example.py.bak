from lookup.ORCID import ORCID
import json

fout = open("orcid_author_details_by_name.txt", "w")

def banner(msg):
    print >> fout, 70 * "="
    print >> fout, msg
    print >> fout, 70 * "=" 
    
banner("orcid author details xml")
print >> fout, ORCID.orcid_author_search("gregor von laszewski", kind="xml").encode('utf-8')

banner("orcid author details json")
print >> fout, json.dumps(ORCID.orcid_author_search("gregor von laszewski", kind="json"), indent=2).encode('utf-8')
