from parsers.ORCID_Parser import ORCID_Parser

from constants.constants import constants
from mongo_load.AuthorLoad import AuthorLoad
from mongo_load.PublicationLoad import PublicationLoad

class LoadToMongoDB:
    @staticmethod
    def load_data_to_mongodb(author_name):
        """
        Method to build a MongoDB database by retrieving the author and publication data from IEEE and ORCID websites
        
        * author_name - the starting point from which the data retrieval starts
        """
        
        if AuthorLoad.find_in_author_search_list(author_name) != 0:
            return 0
        else:
            print 'Authors Count: {0}'.format(AuthorLoad.find_authors_count())
            LoadToMongoDB.search_author_name_and_load_to_mongodb(author_name)
            print 'Authors Count: {0}'.format(AuthorLoad.find_authors_count())
            
            while AuthorLoad.find_authors_count() < constants['retrieve_authors_upto_count'] and PublicationLoad.find_unsearched_publications_count() > 0:
                publication = PublicationLoad.find_unsearched_publication()
                if publication is not None:
                    PublicationLoad.update_publication_as_searched(publication)
                    for author in publication['authors']:
                        LoadToMongoDB.search_author_name_and_load_to_mongodb(author)
                print 'Authors Count: {0}'.format(AuthorLoad.find_authors_count())
            return 1
    
    @staticmethod
    def search_author_name_and_load_to_mongodb(author_name):
        """
        Method to save to MongoDB database all the authors and their works having name similar to given author_name
        """
        
        if AuthorLoad.find_in_author_search_list(author_name) == 0:
            AuthorLoad.save_to_author_search_list(author_name)
            orcid_author_search_results = ORCID_Parser.orcid_author_search_parser(author_name)
            AuthorLoad.save_authors_list(orcid_author_search_results)
        
            while AuthorLoad.find_unsearched_authors_count() > 0:
                author = AuthorLoad.find_unsearched_author()
                if author is not None:
                    AuthorLoad.update_author_as_searched(author)
                    orcid_author_works_get_results = ORCID_Parser.orcid_author_works_get_parser(author['orcid'])
                    PublicationLoad.save_publications_list(orcid_author_works_get_results['works'], orcid_author_works_get_results['orcid'])
