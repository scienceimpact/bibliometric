from scienceimpact.lookup.crossref_author_details import author_details

fout = open("crossref_author_details.txt", "w")

def banner(msg):
    print >>fout,70*"="
    print >>fout,msg
    print >>fout,70*"=" 
    
author = 'Gregor von Laszewski'

banner("crossref author details json")
print >>fout,author_details(author, kind="json")
