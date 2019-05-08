from py2neo import Graph, Node

class PublicationLoad:
    @staticmethod
    def save_publications_list(publications):
        """
        Method to save all the publications to neo4j database
        """
        
        graph = Graph()
        
        for publication in publications:
            publication_node = Node("Publication")
            
            for key in publication:
                if key not in ['_id', 'authorsSearched', 'identifiers', 'rank', 'work-citation-type']:
                    publication_node.properties[key] = publication[key]
            
            graph.create(publication_node)
            print 'Inserted Publication: ' + publication['doi']
