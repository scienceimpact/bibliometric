from lookup.CrossRef import CrossRef

fout = open("crossref_author_details.txt", "w")

def banner(msg):
    print(70 * "=", file=fout)
    print(msg, file=fout)
    print(70 * "=", file=fout) 
    
author = 'Gregor von Laszewski'

banner("crossref author details json")
print(CrossRef.crossref_author_search(author, kind="json"), file=fout)
