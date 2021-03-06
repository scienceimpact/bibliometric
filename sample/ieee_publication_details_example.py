from lookup.IEEE import IEEE
import json

fout = open("ieee_publication_details.txt", "w")

def banner(msg):
    print(70 * "=", file=fout)
    print(msg, file=fout)
    print(70 * "=", file=fout) 
    
publication = 'Abstract Image Management and Universal Image Registration for Cloud and HPC Infrastructures'

banner("ieee author details xml")
print(IEEE.ieee_publication_search(publication, kind="xml").encode('utf-8'), file=fout)

banner("ieee author details json")
print(json.dumps(IEEE.ieee_publication_search(publication, kind="json"), indent=2).encode('utf-8'), file=fout)
