=================== 
Setup Instructions: 
===================

Following is required to start with the setup:

* python
* requests
* xmltodict
* pymongo
* py2neo
* mongodb server
* neo4j server

Instructions:
-------------

* MongoDb and Neo4j servers should be running before starting main.py script.
* MongoDb connects without username or password.
* In case of any change of mongodb settings, constants.py file needs to be changed.
* Currently we are retrieving upto 250 authors which can be changed in constants.py.
* The data is fetched from different websites, parses in required format and loaded into neo4j.
* Cypher queries can then be run on the loaded neo4j database.
* Sample queries are provided in sample_queries.txt
* Options in main.py are as descibed.

*In case of any error while running the code, recreate mongo db and neo4j db before running the code again*  

*The code actually takes time to execute as it is making constant hits to various servers.*
*The time to fetch 250 authors is approximately 30 minutes.*
