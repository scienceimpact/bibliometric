# http://www.informatik.uni-trier.de/~ley/db/

import dblp

authors = dblp.search('Gregor von Laszewski')

for author in authors:
    print author.name

authors = dblp.search('Laszewski')

for author in authors:
    print author.name
    
