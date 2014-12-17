from neo4j_load.AuthorLoad import AuthorLoad
from neo4j_load.PublicationLoad import PublicationLoad
from neo4j_load.RelationshipLoad import RelationshipLoad

from mongo_load.AuthorLoad import AuthorLoad as MongoGetAuthors
from mongo_load.PublicationLoad import PublicationLoad as MongoGetPublications

class LoadToNeo4j:
    @staticmethod
    def load_data_to_neo4j():
        """
        Method to build a Neo4j database by retrieving the author and publication data from MongoDB
        """
        
        authors = MongoGetAuthors.get_all_authors()
        AuthorLoad.save_authors_list(authors)
        
        publications = MongoGetPublications.get_all_publications()
        PublicationLoad.save_publications_list(publications)
        
        RelationshipLoad.save_authored_relationships()
