import dblp

fout = open("author_graph_sample.txt", "w")

authors = dblp.search('Fugang Wang')

visitedAuth = []
authCount = 0

# for auth in authors:
#     print >>fout,auth.name

for auth in authors:
    print >>fout,auth.name
    print >>fout,70*'='
    for pub in auth.publications:
        for a in pub.authors:
            if a not in visitedAuth and a != auth.name:
                visitedAuth.append(a)
                authCount+=1

print >>fout,visitedAuth
fout.write('Author count:'+str(authCount))
        