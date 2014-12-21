Project: Author Name Disambiguation in Bibliographic Data
=========================================================

Team:
===== 
Siddhardha Raju Mandapati, e-mail: siddhardha.rm@gmail.com, github: siddhardha-m;

Amritanshu Joshi, e-mail: amritanshujoshi@gmail.com, github: amritanshujoshi

Description:
============
The main idea of the project is to solve the high ambiguity of the author names in bibliographic data. In most of the technical papers and publications, the authors are identified only by their name. However, different people can have the same full name. So it is a very difficult task to specifically identify the correct person when only the name is provided. The problem becomes even more challenging when the alias names of the authors are provided, as a person can have multiple alias names. We plan to remove the name ambiguity by plotting the authors and publications in a social network graph using authorship as relations between author and publication nodes and then finding the best match of the author of a publication in the graph.

Proposed Solution:
==================

Part 1: Creation of the author social network graph

1.Retrieve the list of all authors uniquely identifying them by an ID and store in a local mongodb database
Author ID Sources: OrcID

2.Retrieve a list of publications with their details of authors etc. and store in a local mongodb database
Publication Data Sources: IEEE

3.Start by picking an author name and retrieving all his publications and all the possible unique IDs for the author.

4.Identify all the co-authors using the publication data. 

5.Use the co-author names in the next iteration to retrieve their publication data. Keep building the data using the co-author relationship, trying to identify the unique ID of each author.

Part 2: Solving the name ambiguity problem

1.Now the problem of specifically identifying an author becomes simply to query the graph data based on his publications or authorship relations as we have tried to uniquely associate each author with unique IDs while building the social network graph.

Technologies Used:
==================
All the programming is done using Python. The data retrieved from various sources is stored in MongoDB and the processed social network graph is stored in Neo4j.

Artifacts and Outcome:
======================
A neo4j graph database containing Authors and Publications as nodes and authorship as relationships between an Author and a Publication node.

Repository on github.com: https://github.com/scienceimpact/bibliometric with all the code, documentation, install instructions and test queries

Testing and Use:
================
Steps to run the project are given here: https://github.com/scienceimpact/bibliometric/blob/master/Installation_Instructions.rst 

The project can be then tested by running cypher queries on the graph data in Neo4j browser

The test cypher queries and the expected outcome are provided here: https://github.com/scienceimpact/bibliometric/blob/master/test_queries.docx 
