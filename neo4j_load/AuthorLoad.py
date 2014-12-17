from py2neo import Graph, Node

class AuthorLoad:
    @staticmethod
    def save_authors_list(authors):
        """
        Method to save all the authors to neo4j database
        """
        
        graph = Graph()
        
        for author in authors:
            author_node = Node("Author")
            
            if 'firstname' in author:
                author_node.properties["firstname"] = author["firstname"]
            if 'lastname' in author:
                author_node.properties["lastname"] = author["lastname"]
            if 'fullname' in author:
                author_node.properties["fullname"] = author["fullname"]
            if 'orcid' in author:
                author_node.properties["orcid"] = author["orcid"]
            if 'othernames' in author:
                author_node.properties["othernames"] = author["othernames"]
            
            graph.create(author_node)
            print 'Inserted Author: ' + author['orcid']
