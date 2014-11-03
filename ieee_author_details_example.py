from scienceimpact.lookup.ieee_author_details import author_details
import json

fout = open("ieee_author_details.txt", "w")

def banner(msg):
    print >>fout,70*"="
    print >>fout,msg
    print >>fout,70*"=" 
    
author = 'Gregor von Laszewski'

banner("ieee author details xml")
print >>fout,author_details(author, kind="xml").encode('utf-8')

banner("ieee author details json")
print >>fout,json.dumps(author_details(author, kind="json"), indent=2).encode('utf-8')
