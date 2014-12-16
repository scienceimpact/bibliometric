"""
* OPTION = 1 - To Load the data to MongoDB by retrieving from ORCID and IEEE websites
* OPTION = 2 - To Load the data to Neo4j by retrieving from MongoDB
"""

from load_data.LoadToMongoDB import LoadToMongoDB

OPTION = 1

def start(option):
    if option == 1:
        load_data_to_mongodb()
    elif option == 2:
        load_data_to_neo4j()

def load_data_to_mongodb():
    author_name = "Gregor von Laszewski"
    LoadToMongoDB.load_data_to_mongodb(author_name)
    print 'Done'
    
def load_data_to_neo4j():
    pass

if __name__ == '__main__' : start(OPTION)
