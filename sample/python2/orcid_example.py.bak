import orcid
from pprint import pprint

authors = orcid.search('laszewski')

print authors

print next(authors).family_name

authors = orcid.search('wang')

print authors

for author in authors:
    a = author.family_name, author.given_name
    print a

gregor = orcid.get('0000-0001-9558-179X')
pprint(gregor)
print gregor.keywords

alfonso = orcid.get('0000-0001-8855-5569')
pprint(alfonso)
print alfonso.keywords
# print alfonso.publications

print gregor.publications()
