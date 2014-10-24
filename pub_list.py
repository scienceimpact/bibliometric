import dblp

authors = dblp.search('Laszewski')

for author in authors:
    for p in author.publications:
        print p.title
