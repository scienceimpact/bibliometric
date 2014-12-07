from py2neo import Graph, Node, Relationship

class LoadIEEEGraph:
    @staticmethod
    def create_graph(pubdict,n):
        
        graph = Graph()
             
        a = Node("Author", name=n)
         
        for key in pubdict.keys():
            li = pubdict[key]
            
            for auth in li:
                if not auth in n:
                    b = Node("Author", name=auth)
                    a_knows_b = Relationship(a, key, b)
                    graph.create(a_knows_b)