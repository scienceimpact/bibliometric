import orcid


authors = orcid.search('laszewski')

print authors

print next(authors).family_name

authors = orcid.search('wang')

print authors

while True:
    a = next(authors).family_name, 
    print a
