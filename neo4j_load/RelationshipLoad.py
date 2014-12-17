from py2neo import Graph

class RelationshipLoad:
    @staticmethod
    def save_authored_relationships():
        """
        Method to save all the authored relationships between Author nodes and Publication nodes
        """
        
        graph = Graph()
        
        graph.cypher.execute("MATCH (a:Author),(p:Publication) WHERE has(a.orcid) and has(p.authorIDs) and any(authorID in p.authorIDs WHERE authorID = a.orcid) CREATE (a)-[:authored]->(p)")
        print 'Inserted authored Relationships'
