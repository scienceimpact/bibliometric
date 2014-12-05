from py2neo import Graph, Node, Relationship

graph = Graph()


a = Node("Author", name="Alice")

b = Node("Author", name="Bob")

a_knows_b = Relationship(a, "CO-AUTHORED", b)

a_knows_b = Relationship(a, "KNOWS", b)

a_knows_b = Relationship(a, "FRIEND", b)

graph.create(a_knows_b)

