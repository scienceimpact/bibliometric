from scienceimpact.lookup.orcid_search_author_details_by_name import author_details
import json

fout = open("orcid_author_details_by_name.txt", "w")

def banner(msg):
    print >>fout,70*"="
    print >>fout,msg
    print >>fout,70*"=" 
    
banner("orcid author details xml")
print >>fout,author_details("gregor von laszewski", kind="xml").encode('utf-8')

banner("orcid author details json")
print >>fout,json.dumps(author_details("gregor von laszewski", kind="json"), indent=2).encode('utf-8')
