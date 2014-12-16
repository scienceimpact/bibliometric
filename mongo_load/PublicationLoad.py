from pymongo import MongoClient
from constants.constants import mongo_constants
from parsers.IEEE_Parser import IEEE_Parser

class PublicationLoad:
    @staticmethod
    def save_publications_list(publications_list, orcid):
        """
        Method to save the list of publications if the publication is not already in the database
        """
        
        client = MongoClient(mongo_constants['server_name'], mongo_constants['port_number'])
        db = client[mongo_constants['database']]
        coll = db[mongo_constants['publication_list']]

        for publication in publications_list:
            if coll.find({'doi': publication['doi']}).count() != 0:
                pub = coll.find_one({'doi': publication['doi']})
                if orcid not in pub['authorIDs']:
                    pub['authorIDs'].append(orcid)
                    coll.update({'doi': pub['doi']}, {"$unset": {'authorIDs': pub['authorIDs']}}, upsert=False, multi=False)
                    coll.update({'doi': pub['doi']}, {"$set": {'authorIDs': pub['authorIDs']}}, upsert=False, multi=False)
            elif coll.find({'title': publication['title']}).count() != 0:
                pub = coll.find_one({'title': publication['title']})
                if orcid not in pub['authorIDs']:
                    pub['authorIDs'].append(orcid)
                    coll.update({'title': pub['title']}, {"$unset": {'authorIDs': pub['authorIDs']}}, upsert=False, multi=False)
                    coll.update({'title': pub['title']}, {"$set": {'authorIDs': pub['authorIDs']}}, upsert=False, multi=False)
            else:
                if orcid not in publication['authorIDs']:
                    publication['authorIDs'].append(orcid)
                if 'doi' in publication:
                    ieee_doi_get_result = IEEE_Parser.ieee_doi_get_parser(publication['doi'])
                    if ieee_doi_get_result is not None:
                        for key in ieee_doi_get_result:
                            if key not in publication:
                                publication[key] = ieee_doi_get_result[key]
                        if 'authors' in ieee_doi_get_result:
                            publication['authorsIeee'] = ieee_doi_get_result['authors']
                publication['authorsSearched'] = 0
                coll.insert(publication)
    
    @staticmethod
    def find_unsearched_publication():
        """
        Method to find a publication for which the authors haven't been searched
        """
        
        client = MongoClient(mongo_constants['server_name'], mongo_constants['port_number'])
        db = client[mongo_constants['database']]
        coll = db[mongo_constants['publication_list']]

        return coll.find_one({'authorsSearched': 0})
    
    @staticmethod
    def find_unsearched_publications_count():
        """
        Method to find the count of publications for which the authors haven't been searched
        """
        
        client = MongoClient(mongo_constants['server_name'], mongo_constants['port_number'])
        db = client[mongo_constants['database']]
        coll = db[mongo_constants['publication_list']]

        return coll.find({'authorsSearched': 0}).count()
    
    @staticmethod
    def update_publication_as_searched(publication):
        """
        Method to update a publication as searched for its authors
        """
        
        client = MongoClient(mongo_constants['server_name'], mongo_constants['port_number'])
        db = client[mongo_constants['database']]
        coll = db[mongo_constants['publication_list']]

        coll.update({'_id': publication['_id']}, {"$set": {'authorsSearched': 1}}, upsert=False, multi=False)
