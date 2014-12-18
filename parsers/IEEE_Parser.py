import xml.etree.ElementTree as ET

from lookup.IEEE import IEEE

class IEEE_Parser:
    @staticmethod
    def ieee_author_search_parser(author_name):
        """
        Method to parse the list of publications and their authors from IEEE website into an array object, given the name of the author
        """
        
        out_file = "data/ieee_author_search.xml"
        fout = open(out_file, "w")
        print >> fout, IEEE.ieee_author_search(author_name, kind="xml").encode('utf-8')
        fout.close()
        
        tree = ET.parse(out_file)
        root_element = tree.getroot()

        publications = []

        for child1 in root_element:
            if(child1.tag == 'document'):
                title = None
                authors = []
                publication = {}
                for child2 in child1:
                    if(child2.tag == 'title'):
                        title = child2.text
                    elif(child2.tag == 'authors'):
                        authors = IEEE_Parser.format_names_list(child2.text)
                if title is not None:
                    publication['title'] = title
                    publication['authors'] = authors
                publications.append(publication)
        
        return publications

    @staticmethod
    def format_names_list(names):
        """
        Method to parse the author names list to proper format (i.e. 'von Laszewski, G.' as 'G. von Laszewski') 
        """
        parsedNamesList = []

        if names is not None:
            namesList = names.split(';  ')
        
            for name in namesList:
                firstname = ''
                lastname = ''
                if ', ' in name:
                    lastname = name[:name.index(',')]
                    firstname = name[name.index(', ')+2:]
                else:
                    if(name.find(' ') > -1):
                        firstname = name[:name.index(' ')]
                        lastname = name[name.index(' ')+1:]
                    
                parsedNamesList.append(firstname + ' ' + lastname)
                
        return parsedNamesList
    
    @staticmethod
    def ieee_publication_search_parser(publication_name):
        """
        Method to parse the publication details from IEEE website into an array object, given the name of the publication
        """
        
        out_file = "data/ieee_publication_search.xml"
        fout = open(out_file, "w")
        print >> fout, IEEE.ieee_publication_search(publication_name, kind="xml").encode('utf-8')
        fout.close()
        
        tree = ET.parse(out_file)
        root_element = tree.getroot()

        publications = []
        
        for child1 in root_element:
            if(child1.tag == 'document'):
                publication = {}
                for child2 in child1:
                    if(child2.tag == 'rank'):
                        publication['rank'] = child2.text
                    elif(child2.tag == 'title'):
                        publication['title'] = child2.text
                    elif(child2.tag == 'authors'):
                        publication['authors'] = IEEE_Parser.format_names_list(child2.text)
                    elif(child2.tag == 'pubtitle'):
                        publication['pubtitle'] = child2.text
                    elif(child2.tag == 'punumber'):
                        publication['pubnumber'] = child2.text
                    elif(child2.tag == 'pubtype'):
                        publication['pubtype'] = child2.text
                    elif(child2.tag == 'publisher'):
                        publication['publisher'] = child2.text
                    elif(child2.tag == 'py'):
                        publication['pubyear'] = child2.text
                    elif(child2.tag == 'isbn'):
                        publication['isbn'] = child2.text
                    elif(child2.tag == 'arnumber'):
                        publication['arnumber'] = child2.text                        
                    elif(child2.tag == 'doi'):
                        publication['doi'] = child2.text
                    elif(child2.tag == 'publicationId'):
                        publication['publicationId'] = child2.text
                if 'doi' not in publication:
                    publication['doi'] = ''
                publications.append(publication)
        
        return publications
    
    @staticmethod
    def ieee_doi_get_parser(doi_number):
        """
        Method to parse the publication details from IEEE website into a dictionary object, given the DOI number
        """
        
        out_file = "data/ieee_doi_get.xml"
        fout = open(out_file, "w")
        print >> fout, IEEE.ieee_doi_get(doi_number, kind="xml").encode('utf-8')
        fout.close()
        
        tree = ET.parse(out_file)
        root_element = tree.getroot()

        publication = {}
        
        for child1 in root_element:
            if(child1.tag == 'document'):
                for child2 in child1:
                    if(child2.tag == 'rank'):
                        publication['rank'] = child2.text
                    elif(child2.tag == 'title'):
                        publication['title'] = child2.text
                    elif(child2.tag == 'authors'):
                        publication['authors'] = IEEE_Parser.format_names_list(child2.text)
                    elif(child2.tag == 'pubtitle'):
                        publication['pubtitle'] = child2.text
                    elif(child2.tag == 'punumber'):
                        publication['pubnumber'] = child2.text
                    elif(child2.tag == 'pubtype'):
                        publication['pubtype'] = child2.text
                    elif(child2.tag == 'publisher'):
                        publication['publisher'] = child2.text
                    elif(child2.tag == 'py'):
                        publication['pubyear'] = child2.text
                    elif(child2.tag == 'isbn'):
                        publication['isbn'] = child2.text
                    elif(child2.tag == 'arnumber'):
                        publication['arnumber'] = child2.text                        
                    elif(child2.tag == 'doi'):
                        publication['doi'] = child2.text
                    elif(child2.tag == 'publicationId'):
                        publication['publicationId'] = child2.text
        
        return publication
