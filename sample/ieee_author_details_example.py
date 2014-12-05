from lookup.IEEE import IEEE
import json

fout = open("ieee_author_details.txt", "w")

def banner(msg):
    print >>fout,70*"="
    print >>fout,msg
    print >>fout,70*"=" 
    
author = 'Gregor von Laszewski'

banner("ieee author details xml")
print >>fout,IEEE.ieee_author_search(author, kind="xml").encode('utf-8')

banner("ieee author details json")
print >>fout,json.dumps(IEEE.ieee_author_search(author, kind="json"), indent=2).encode('utf-8')
