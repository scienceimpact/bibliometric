import dblp

authors = dblp.search('Gregor von Laszewski')

#for author in authors:
#    print author.name
    
for author in authors:
    print 70*"="
    print author.name
    print 70*"="
    for pub in author.publications:
        print '"Key" : "{}", "Title" : "{}", "ISBN" : "{}", "ee" : "{}", "crossref" : "{}", "month" : "{}", "year" : "{}", "mdate" : "{}", "booktitle" : "{}", '\
        '"type" : "{}", "sub_type" : "{}", "journal" : "{}", "volume" : "{}", "number" : "{}", "chapter" : "{}", "school" : "{}", "url" : "{}", '\
        '"authors" : "{}", "editors" : "{}", "citations" : "{}", "publisher" : "{}", "series" : "{}", "pages" : "{}"'.format(
        pub.key, pub.title, pub.isbn, pub.ee, pub.crossref, pub.month, pub.year, pub.mdate, pub.booktitle,
        pub.type, pub.sub_type, pub.journal, pub.volume, pub.number, pub.chapter, pub.school, pub.url,
        pub.authors, pub.editors, pub.citations, pub.publisher, pub.series, pub.pages
        )
