import dblp

fout = open("dblp_author_search_details.txt", "w")

authors = dblp.search('Gregor von Laszewski')

# for author in authors:
#    print author.name

try:
    for author in authors:
        print >> fout, 70 * "="
        print >> fout, author.name
        print >> fout, 70 * "="
        for pub in author.publications:
            print >> fout, '"Key" : "{}", "Title" : "{}", "ISBN" : "{}", "ee" : "{}", "crossref" : "{}", "month" : "{}", "year" : "{}", "mdate" : "{}", "booktitle" : "{}", '\
            '"type" : "{}", "sub_type" : "{}", "journal" : "{}", "volume" : "{}", "number" : "{}", "chapter" : "{}", "school" : "{}", "url" : "{}", '\
            '"authors" : "{}", "editors" : "{}", "citations" : "{}", "publisher" : "{}", "series" : "{}", "pages" : "{}"'.format(
            pub.key, pub.title, pub.isbn, pub.ee, pub.crossref, pub.month, pub.year, pub.mdate, pub.booktitle,
            pub.type, pub.sub_type, pub.journal, pub.volume, pub.number, pub.chapter, pub.school, pub.url,
            pub.authors, pub.editors, pub.citations, pub.publisher, pub.series, pub.pages
            )
except:
    pass
