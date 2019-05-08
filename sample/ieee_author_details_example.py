from lookup.IEEE import IEEE
import json

fout = open("ieee_author_details.txt", "w")

def banner(msg):
    print(70 * "=", file=fout)
    print(msg, file=fout)
    print(70 * "=", file=fout) 
    
author = 'Gregor von Laszewski'

banner("ieee author details xml")
print(IEEE.ieee_author_search(author, kind="xml").encode('utf-8'), file=fout)

banner("ieee author details json")
print(json.dumps(IEEE.ieee_author_search(author, kind="json"), indent=2).encode('utf-8'), file=fout)
