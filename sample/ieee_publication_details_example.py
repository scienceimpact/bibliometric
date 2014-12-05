from lookup.IEEE import IEEE
import json

fout = open("ieee_publication_details.txt", "w")

def banner(msg):
    print >>fout,70*"="
    print >>fout,msg
    print >>fout,70*"=" 
    
publication = 'Abstract Image Management and Universal Image Registration for Cloud and HPC Infrastructures'

banner("ieee author details xml")
print >>fout,IEEE.ieee_publication_search(publication, kind="xml").encode('utf-8')

banner("ieee author details json")
print >>fout,json.dumps(IEEE.ieee_publication_search(publication, kind="json"), indent=2).encode('utf-8')
