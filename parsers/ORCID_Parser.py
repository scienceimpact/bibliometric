import xml.etree.ElementTree as ET
import re

from lookup.ORCID import ORCID
from parsers.IEEE_Parser import IEEE_Parser

class ORCID_Parser:
    @staticmethod
    def orcid_author_get_parser(orcid):
        """
        Method to parse the author details from ORCID website into a dictionary object, given the orcid of the author
        """
        
        out_file = "../data/orcid_author_get.xml"
        fout = open(out_file, "w")
        print >> fout, ORCID.orcid_author_get(orcid, kind="xml").encode('utf-8')
        fout.close()
        
        tree = ET.parse(out_file)
        root_element = tree.getroot()
        ns = '{http://www.orcid.org/ns/orcid}'
        
        author = {'othernames': [], 'urls': [], 'identifiers': []}
        
        for child1 in root_element:
            if(child1.tag == ns + 'orcid-profile'):
                for child2 in child1:
                    if(child2.tag == ns + 'orcid-identifier'):
                        for child3 in child2:
                            if(child3.tag == ns + 'path'):
                                author['orcid'] = child3.text
                    elif(child2.tag == ns + 'orcid-bio'):
                        for child3 in child2:
                            if(child3.tag == ns + 'personal-details'):
                                for child4 in child3:
                                    if(child4.tag == ns + 'given-names'):
                                        author['firstname'] = child4.text
                                    elif(child4.tag == ns + 'family-name'):
                                        author['lastname'] = child4.text
                                    elif(child4.tag == ns + 'other-names'):
                                        for child5 in child4:
                                            if(child5.tag == ns + 'other-name'):
                                                author['othernames'].append(child5.text)
                            elif(child3.tag == ns + 'researcher-urls'):
                                for child4 in child3:
                                    if(child4.tag == ns + 'researcher-url'):
                                        for child5 in child4:
                                            if(child5.tag == ns + 'url'):
                                                author['urls'].append(child5.text)
                            elif(child3.tag == ns + 'contact-details'):
                                for child4 in child3:
                                    if(child4.tag == ns + 'email'):
                                        author['email'] = child4.text
                            elif(child3.tag == ns + 'external-identifiers'):
                                for child4 in child3:
                                    if(child4.tag == ns + 'external-identifier'):
                                        identifier = {}
                                        for child5 in child4:
                                            if(child5.tag == ns + 'external-id-common-name'):
                                                key = None
                                                if(child5.text == 'ResearcherID'):
                                                    key = 'ResearcherID'
                                                elif(child5.text == 'Scopus Author ID'):
                                                    key = 'ScopusID'
                                            elif(child5.tag == ns + 'external-id-reference'):
                                                value = child5.text
                                        if key is not None:
                                            identifier[key] = value
                                        author['identifiers'].append(identifier)
        
        return author
    
    @staticmethod
    def orcid_author_works_get_parser(orcid):
        """
        Method to parse the author works from ORCID website into a dictionary object, given the orcid of the author
        """
        
        out_file = "../data/orcid_author_works_get.xml"
        fout = open(out_file, "w")
        print >> fout, ORCID.orcid_author_works_get(orcid, kind="xml").encode('utf-8')
        fout.close()
        
        tree = ET.parse(out_file)
        root_element = tree.getroot()
        ns = '{http://www.orcid.org/ns/orcid}'
        
        author = {'works': []}
        
        for child1 in root_element:
            if(child1.tag == ns + 'orcid-profile'):
                for child2 in child1:
                    if(child2.tag == ns + 'orcid-identifier'):
                        for child3 in child2:
                            if(child3.tag == ns + 'path'):
                                author['orcid'] = child3.text
                    elif(child2.tag == ns + 'orcid-activities'):
                        for child3 in child2:
                            if(child3.tag == ns + 'orcid-works'):
                                for child4 in child3:
                                    if(child4.tag == ns + 'orcid-work'):
                                        work = {'identifiers': [], 'authorIDs': []}
                                        for child5 in child4:
                                            if(child5.tag == ns + 'work-title'):
                                                for child6 in child5:
                                                    if(child6.tag == ns + 'title'):
                                                        work['title'] = child6.text
                                            elif(child5.tag == ns + 'journal-title'):
                                                work['journalTitle'] = child5.text
                                            elif(child5.tag == ns + 'work-citation'):
                                                for child6 in child5:
                                                    if(child6.tag == ns + 'work-citation-type'):
                                                        work['work-citation-type'] = child6.text
                                                    elif(child6.tag == ns + 'citation'):
                                                        citation = child6.text
                                                
                                                if(work['work-citation-type'] == 'bibtex'):
                                                    work['authors'] = ORCID_Parser.get_authors_list_from_bibtex(citation)
                                                elif(work['work-citation-type'] == 'formatted-unspecified'):
                                                    work['authors'] = ORCID_Parser.get_authors_list_from_unformattedtext(citation)
                                            elif(child5.tag == ns + 'publication-date'):
                                                for child6 in child5:
                                                    if(child6.tag == ns + 'year'):
                                                        work['year'] = child6.text
                                            elif(child5.tag == ns + 'work-external-identifiers'):
                                                for child6 in child5:
                                                    if(child6.tag == ns + 'work-external-identifier'):
                                                        identifier = {}
                                                        for child7 in child6:
                                                            if(child7.tag == ns + 'work-external-identifier-type'):
                                                                key = None
                                                                if(child7.text == 'doi'):
                                                                    key = 'doi'
                                                            elif(child7.tag == ns + 'work-external-identifier-id'):
                                                                value = child7.text
                                                        
                                                        if key is not None:
                                                            identifier[key] = value
                                                            work[key] = value
                                                        work['identifiers'].append(identifier)
                                        
                                        if 'title' not in work:
                                            work['title'] = ''
                                        if 'doi' not in work:
                                            publications = IEEE_Parser.ieee_publication_search_parser(work['title'])
                                            if(len(publications) == 1):
                                                for publication in publications:
                                                    work['doi'] = publication['doi']
                                            else:
                                                work['doi'] = ''
                                        if 'authors' not in work:
                                            work['authors'] = []
                                        author['works'].append(work)
        
        return author
    
    @staticmethod
    def orcid_author_search_parser(author_name):
        """
        Method to parse the list of matching authors from ORCID website into an array object, given the name of the author
        """
        
        out_file = "../data/orcid_author_search.xml"
        fout = open(out_file, "w")
        print >> fout, ORCID.orcid_author_search(author_name, kind="xml").encode('utf-8')
        fout.close()
        
        tree = ET.parse(out_file)
        root_element = tree.getroot()
        ns = '{http://www.orcid.org/ns/orcid}'
        
        authors = []
        
        for child1 in root_element:
            if(child1.tag == ns + 'orcid-search-results'):
                for child2 in child1:
                    if(child2.tag == ns + 'orcid-search-result'):
                        author = {'othernames': []}
                        for child3 in child2:
                            if(child3.tag == ns + 'orcid-profile'):
                                for child4 in child3:
                                    if(child4.tag == ns + 'orcid-identifier'):
                                        for child5 in child4:
                                            if(child5.tag == ns + 'path'):
                                                author['orcid'] = child5.text
                                    elif(child4.tag == ns + 'orcid-bio'):
                                        for child5 in child4:
                                            if(child5.tag == ns + 'personal-details'):
                                                for child6 in child5:
                                                    if(child6.tag == ns + 'given-names'):
                                                        author['firstname'] = child6.text
                                                    elif(child6.tag == ns + 'family-name'):
                                                        author['lastname'] = child6.text
                                                    elif(child6.tag == ns + 'other-names'):
                                                        for child7 in child6:
                                                            if(child7.tag == ns + 'other-name'):
                                                                author['othernames'].append(child7.text)
                        
                        author = ORCID_Parser.generate_author_other_names(author)
                        authors.append(author)
        
        return authors
    
    @staticmethod
    def generate_author_other_names(author):
        """
        Method to generate all the possible other names for the author from the first name and the last name 
        """
        
        firstname = ''
        lastname = ''
        if 'firstname' in author:
            firstname = author['firstname']
        if 'lastname' in author:
            lastname = author['lastname']
        
        fullname = firstname + ' ' + lastname
        
        fullname = fullname.replace('.', '')
        fullname = fullname.replace('-', ' ')
        
        nameslist = fullname.split()
        
        for n in nameslist:
            author['othernames'].append(n)
            
            others = [a for a in nameslist if a != n]
            othername = n[0] + ' ' + ' '.join(others)
            author['othernames'].append(othername)
            
            for m in others:
                others2 = [b for b in others if b!= m]
                othername = n[0] + ' ' + m[0] + ' ' + ' '.join(others2)
                author['othernames'].append(othername)
                
                for l in others2:
                    others3 = [c for c in others2 if c != l]
                    othername = n[0] + ' ' + m[0] + ' ' + l[0] + ' ' + ' '.join(others3)
                    author['othernames'].append(othername)
        
        author['fullname'] = fullname
        
        return author
    
    @staticmethod
    def get_authors_list_from_bibtex(citation_text):
        """
        Method to parse the citation text in bibtex format and return the list of authors
        """
        authors = []
        if citation_text.find('author = {') != -1:
            authors = citation_text[citation_text.find('author = {')+10:citation_text.find('}', citation_text.find('author = {')+10)].split('and')
            authors = [author_name.strip() for author_name in authors]
        return authors
        
    @staticmethod
    def get_authors_list_from_unformattedtext(citation_text):
        """
        Method to parse the unformatted citation text and return the list of authors
        """
        authors = []
        if re.search("\d", citation_text) is not None:
            authors = citation_text[:re.search("\d", citation_text).start()-2]
        
            if re.search(", [A-z],", citation_text) is None:
                authors = authors.split(',')
                authors = [author_name.strip() for author_name in authors]
            elif re.search("&", citation_text) is None:
                authors = [authors]
            else:
                authors = authors.replace(' &', ',')
                splitIndexes = [matchIndex.start()+4 for matchIndex in re.finditer(", [A-z],", authors)]
                
                authorsList = []
                
                startIndex = 0
                
                for index in splitIndexes:
                    endIndex = index 
                    author_name = authors[startIndex:endIndex-1]
                    authorsList.append(author_name)
                    startIndex = endIndex
                author_name = authors[startIndex:]
                authorsList.append(author_name)
                
                authors = authorsList
                authors = [author_name.strip() for author_name in authors]
        
        return authors
