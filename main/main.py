"""
* OPTION = "load_data" - First load the data to MongoDB by retrieving from ORCID and IEEE websites
                         Next load the data to Neo4j by retrieving from MongoDB
                         It is combination of the options "load_mongodb" and "load_neo4j"
                         
* OPTION = "load_mongodb" - To load the data to MongoDB by retrieving from ORCID and IEEE websites
* OPTION = "load_neo4j" - To load the data to Neo4j by retrieving from MongoDB
"""

OPTION = "load_data"
author_name = "Gregor von Laszewski"

from load_data.LoadToMongoDB import LoadToMongoDB
from load_data.LoadToNeo4j import LoadToNeo4j

def start(option):
    if option == "load_data":
        load_data()
    elif option == "load_mongodb":
        load_data_to_mongodb()
    elif option == "load_neo4j":
        load_data_to_neo4j()
    else:
        print 'Invalid option given'

def load_data():
    print 'Started loading data'
    return_value = load_data_to_mongodb()
    if return_value == 1:
        load_data_to_neo4j()
    else:
        print 'Skipped loading data to Neo4j'
    print 'Finished loading data'

def load_data_to_mongodb():
    print 'Started loading data to MongoDB'
    return_value = LoadToMongoDB.load_data_to_mongodb(author_name)
    if return_value == 1:
        print 'Finished loading data to MongoDB'
    else:
        print 'Error: Skipped loading data to MongoDB. The given starting point author_name "{0}" is already present in the database. Give a different author_name in main.py'.format(author_name)
    return return_value
    
def load_data_to_neo4j():
    print 'Started loading data to Neo4j'
    LoadToNeo4j.load_data_to_neo4j()
    print 'Finished loading data to Neo4j'

if __name__ == '__main__' : start(OPTION)
