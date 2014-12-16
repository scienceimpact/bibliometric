from pymongo import MongoClient
from constants.constants import mongo_constants

class AuthorLoad:
    @staticmethod
    def save_to_author_search_list(author_name):
        """
        Method to save an author_name which has been searched
        """
        
        client = MongoClient(mongo_constants['server_name'], mongo_constants['port_number'])
        db = client[mongo_constants['database']]
        coll = db[mongo_constants['author_search_list']]

        doc = {'author_name': author_name}
        
        coll.insert(doc)
    
    @staticmethod
    def find_in_author_search_list(author_name):
        """
        Method to find if an author_name has already been searched
        
        Returns the count of number of documents matching the author_name
        """
        
        client = MongoClient(mongo_constants['server_name'], mongo_constants['port_number'])
        db = client[mongo_constants['database']]
        coll = db[mongo_constants['author_search_list']]
        
        doc = {'author_name': author_name}

        return coll.find(doc).count()
    
    @staticmethod
    def save_authors_list(authors_list):
        """
        Method to save the list of authors if the author is not already in the database
        """
        
        client = MongoClient(mongo_constants['server_name'], mongo_constants['port_number'])
        db = client[mongo_constants['database']]
        coll = db[mongo_constants['author_list']]

        for author in authors_list:
            if coll.find({'orcid': author['orcid']}).count() == 0:
                author['worksFound'] = 0
                coll.insert(author)
    
    @staticmethod
    def find_unsearched_author():
        """
        Method to find an author for whom the publications haven't been searched
        """
        
        client = MongoClient(mongo_constants['server_name'], mongo_constants['port_number'])
        db = client[mongo_constants['database']]
        coll = db[mongo_constants['author_list']]

        return coll.find_one({'worksFound': 0})
    
    @staticmethod
    def find_unsearched_authors_count():
        """
        Method to find the count of authors for whom the publications haven't been searched
        """
        
        client = MongoClient(mongo_constants['server_name'], mongo_constants['port_number'])
        db = client[mongo_constants['database']]
        coll = db[mongo_constants['author_list']]

        return coll.find({'worksFound': 0}).count()
    
    @staticmethod
    def update_author_as_searched(author):
        """
        Method to update an author as searched for his publications
        """
        
        client = MongoClient(mongo_constants['server_name'], mongo_constants['port_number'])
        db = client[mongo_constants['database']]
        coll = db[mongo_constants['author_list']]

        coll.update({'_id': author['_id']}, {"$set": {'worksFound': 1}}, upsert=False, multi=False)
    
    @staticmethod
    def find_authors_count():
        """
        Method to find the count of authors in the database
        """
        
        client = MongoClient(mongo_constants['server_name'], mongo_constants['port_number'])
        db = client[mongo_constants['database']]
        coll = db[mongo_constants['author_list']]

        return coll.count()
