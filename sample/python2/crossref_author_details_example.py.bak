from lookup.CrossRef import CrossRef

fout = open("crossref_author_details.txt", "w")

def banner(msg):
    print >> fout, 70 * "="
    print >> fout, msg
    print >> fout, 70 * "=" 
    
author = 'Gregor von Laszewski'

banner("crossref author details json")
print >> fout, CrossRef.crossref_author_search(author, kind="json")
