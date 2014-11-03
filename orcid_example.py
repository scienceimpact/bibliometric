import orcid

authors = orcid.search('laszewski')

print authors

print next(authors).family_name

authors = orcid.search('wang')

print authors

for author in authors:
    a = author.family_name, 
    print a
